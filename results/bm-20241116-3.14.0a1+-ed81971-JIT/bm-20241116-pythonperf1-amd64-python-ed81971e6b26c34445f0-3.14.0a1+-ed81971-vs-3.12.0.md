# Results vs. 3.12.0

- fork: python
- ref: ed81971e6b26c34445f0
- machine: windows-amd64
- commit hash: ed81971
- commit date: 2024-11-16
- overall geometric mean: 1.026x faster
- HPT reliability: 90.36%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 244 ms: 1.12x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.89 sec: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 245 ms: 1.49x faster                                                        |
| async_tree_none            | 291 ms                                                      | 208 ms: 1.40x faster                                                        |
| async_tree_io              | 731 ms                                                      | 546 ms: 1.34x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 263 ms: 1.29x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 221 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 401 ms: 1.25x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 391 ms: 1.25x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 622 ms: 1.24x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.32x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 55.9 ms: 1.29x faster                                                       |
| float          | 56.8 ms                                                     | 47.4 ms: 1.20x faster                                                       |
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.03x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.4 ms: 1.01x slower                                                       |
| regex_compile  | 87.5 ms                                                     | 90.3 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                     | 50.7 ms: 1.10x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.25 sec: 1.10x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 35.7 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.1 ms: 1.05x faster                                                       |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 205 us: 1.05x slower                                                        |
| unpickle_pure_python | 133 us                                                      | 141 us: 1.06x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.25 ms: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.6 ms: 1.08x slower                                                       |
| python_startup         | 19.5 ms                                                     | 23.3 ms: 1.20x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.12 ms: 1.38x faster                                                       |
| django_template | 22.9 ms                                                     | 26.8 ms: 1.17x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 245 ms: 1.49x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 16.1 us: 1.47x faster                                                       |
| async_tree_none            | 291 ms                                                      | 208 ms: 1.40x faster                                                        |
| mako                       | 7.09 ms                                                     | 5.12 ms: 1.38x faster                                                       |
| async_tree_io              | 731 ms                                                      | 546 ms: 1.34x faster                                                        |
| spectral_norm              | 66.9 ms                                                     | 51.6 ms: 1.30x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 263 ms: 1.29x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 221 ms: 1.29x faster                                                        |
| nbody                      | 71.9 ms                                                     | 55.9 ms: 1.29x faster                                                       |
| deepcopy                   | 238 us                                                      | 187 us: 1.28x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 401 ms: 1.25x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 391 ms: 1.25x faster                                                        |
| scimark_sor                | 78.8 ms                                                     | 63.3 ms: 1.24x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 622 ms: 1.24x faster                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 39.9 ms: 1.21x faster                                                       |
| float                      | 56.8 ms                                                     | 47.4 ms: 1.20x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.14 ms: 1.19x faster                                                       |
| scimark_fft                | 184 ms                                                      | 155 ms: 1.19x faster                                                        |
| comprehensions             | 14.1 us                                                     | 11.9 us: 1.19x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 37.1 ms: 1.18x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.86 us: 1.13x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 52.3 ms: 1.13x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 39.5 ms: 1.12x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 461 ms: 1.11x faster                                                        |
| pprint_pformat             | 1.05 sec                                                    | 942 ms: 1.11x faster                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 50.7 ms: 1.10x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 55.0 ns: 1.10x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.25 sec: 1.10x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.61 us: 1.10x faster                                                       |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| pathlib                    | 80.5 ms                                                     | 75.0 ms: 1.07x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.4 ms: 1.06x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 35.7 ms: 1.06x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 811 us: 1.06x faster                                                        |
| chaos                      | 43.3 ms                                                     | 41.3 ms: 1.05x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.1 ms: 1.05x faster                                                       |
| json                       | 3.05 ms                                                     | 2.92 ms: 1.05x faster                                                       |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| meteor_contest             | 74.6 ms                                                     | 72.0 ms: 1.04x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.54 us: 1.03x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.03x faster                                                       |
| fannkuch                   | 247 ms                                                      | 241 ms: 1.02x faster                                                        |
| logging_simple             | 6.28 us                                                     | 6.14 us: 1.02x faster                                                       |
| go                         | 91.6 ms                                                     | 90.2 ms: 1.02x faster                                                       |
| generators                 | 22.5 ms                                                     | 22.8 ms: 1.01x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.4 ms: 1.01x slower                                                       |
| pycparser                  | 699 ms                                                      | 714 ms: 1.02x slower                                                        |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 90.3 ms: 1.03x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 65.3 ms: 1.04x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.32 ms: 1.05x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 205 us: 1.05x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 141 us: 1.06x slower                                                        |
| sympy_str                  | 175 ms                                                      | 188 ms: 1.07x slower                                                        |
| deltablue                  | 2.16 ms                                                     | 2.33 ms: 1.08x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 17.6 ms: 1.08x slower                                                       |
| pyflate                    | 295 ms                                                      | 321 ms: 1.09x slower                                                        |
| sqlglot_parse              | 804 us                                                      | 880 us: 1.09x slower                                                        |
| json_dumps                 | 5.70 ms                                                     | 6.25 ms: 1.10x slower                                                       |
| async_generators           | 239 ms                                                      | 263 ms: 1.10x slower                                                        |
| sympy_sum                  | 91.5 ms                                                     | 101 ms: 1.10x slower                                                        |
| sqlglot_normalize          | 187 ms                                                      | 208 ms: 1.11x slower                                                        |
| 2to3                       | 218 ms                                                      | 244 ms: 1.12x slower                                                        |
| sympy_expand               | 284 ms                                                      | 318 ms: 1.12x slower                                                        |
| docutils                   | 1.66 sec                                                    | 1.89 sec: 1.14x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.16 ms: 1.14x slower                                                       |
| raytrace                   | 192 ms                                                      | 221 ms: 1.15x slower                                                        |
| coverage                   | 40.8 ms                                                     | 47.2 ms: 1.15x slower                                                       |
| django_template            | 22.9 ms                                                     | 26.8 ms: 1.17x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.63 sec: 1.19x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 15.4 ms: 1.19x slower                                                       |
| python_startup             | 19.5 ms                                                     | 23.3 ms: 1.20x slower                                                       |
| richards_super             | 32.1 ms                                                     | 38.5 ms: 1.20x slower                                                       |
| richards                   | 28.4 ms                                                     | 34.2 ms: 1.21x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 116 us: 1.22x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 42.9 ms: 1.24x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.91 ms: 1.25x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 87.0 ms: 1.26x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 5.18 ms: 1.26x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.39 ms: 1.85x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_parse
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241116-3.14.0a1+-ed81971-JIT/bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.026x faster
# HPT report

- Reliability score: 90.36% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown