# Results vs. 3.12.0

- fork: python
- ref: ed81971e6b26c34445f0
- machine: windows-amd64
- commit hash: ed81971
- commit date: 2024-11-16
- overall geometric mean: 1.025x slower
- HPT reliability: 99.54%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 224 ms: 1.03x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 258 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 211 ms: 1.35x faster                                                        |
| async_tree_none            | 291 ms                                                      | 221 ms: 1.32x faster                                                        |
| async_tree_io              | 731 ms                                                      | 558 ms: 1.31x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 385 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 402 ms: 1.25x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 628 ms: 1.23x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 277 ms: 1.23x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.30x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 145 ms: 1.05x faster                                                        |
| float          | 56.8 ms                                                     | 56.4 ms: 1.01x faster                                                       |
| nbody          | 71.9 ms                                                     | 82.8 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                       |
| regex_dna      | 126 ms                                                      | 124 ms: 1.02x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 91.2 ms: 1.04x slower                                                       |
| regex_v8       | 14.2 ms                                                     | 15.2 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 65.9 ms: 1.01x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.04x slower                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 96.8 ms: 1.04x slower                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 59.2 ms: 1.06x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 41.2 ms: 1.09x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.58 sec: 1.16x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 227 us: 1.16x slower                                                        |
| unpickle_pure_python | 133 us                                                      | 155 us: 1.17x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.66 ms: 1.17x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.10x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.9 ms: 1.10x slower                                                       |
| python_startup         | 19.5 ms                                                     | 24.0 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.17x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.95 ms: 1.02x faster                                                       |
| django_template | 22.9 ms                                                     | 25.4 ms: 1.11x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 258 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 211 ms: 1.35x faster                                                        |
| async_tree_none            | 291 ms                                                      | 221 ms: 1.32x faster                                                        |
| async_tree_io              | 731 ms                                                      | 558 ms: 1.31x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 385 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 402 ms: 1.25x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 628 ms: 1.23x faster                                                        |
| deepcopy                   | 238 us                                                      | 194 us: 1.23x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 277 ms: 1.23x faster                                                        |
| comprehensions             | 14.1 us                                                     | 12.4 us: 1.14x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 21.3 us: 1.11x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 74.5 ms: 1.08x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.63 us: 1.08x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.98 us: 1.06x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 816 us: 1.05x faster                                                        |
| pidigits                   | 152 ms                                                      | 145 ms: 1.05x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.7 ms: 1.04x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.9 ms: 1.03x faster                                                       |
| generators                 | 22.5 ms                                                     | 21.9 ms: 1.03x faster                                                       |
| regex_dna                  | 126 ms                                                      | 124 ms: 1.02x faster                                                        |
| sympy_sum                  | 91.5 ms                                                     | 89.7 ms: 1.02x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.95 ms: 1.02x faster                                                       |
| go                         | 91.6 ms                                                     | 90.2 ms: 1.02x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 48.1 ms: 1.01x faster                                                       |
| float                      | 56.8 ms                                                     | 56.4 ms: 1.01x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 63.3 ms: 1.01x slower                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 65.9 ms: 1.01x slower                                                       |
| spectral_norm              | 66.9 ms                                                     | 67.8 ms: 1.01x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.82 us: 1.02x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.39 us: 1.02x slower                                                       |
| sympy_str                  | 175 ms                                                      | 179 ms: 1.02x slower                                                        |
| async_generators           | 239 ms                                                      | 245 ms: 1.02x slower                                                        |
| raytrace                   | 192 ms                                                      | 197 ms: 1.03x slower                                                        |
| docutils                   | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                      |
| 2to3                       | 218 ms                                                      | 224 ms: 1.03x slower                                                        |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.04x slower                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 96.8 ms: 1.04x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.5 ms: 1.04x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 91.2 ms: 1.04x slower                                                       |
| pycparser                  | 699 ms                                                      | 741 ms: 1.06x slower                                                        |
| deltablue                  | 2.16 ms                                                     | 2.29 ms: 1.06x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 59.2 ms: 1.06x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 79.3 ms: 1.06x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 200 ms: 1.07x slower                                                        |
| regex_v8                   | 14.2 ms                                                     | 15.2 ms: 1.07x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.12 sec: 1.07x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 37.1 ms: 1.08x slower                                                       |
| scimark_fft                | 184 ms                                                      | 200 ms: 1.08x slower                                                        |
| logging_silent             | 60.5 ns                                                     | 65.5 ns: 1.08x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 558 ms: 1.09x slower                                                        |
| sympy_expand               | 284 ms                                                      | 309 ms: 1.09x slower                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 47.7 ms: 1.09x slower                                                       |
| pyflate                    | 295 ms                                                      | 321 ms: 1.09x slower                                                        |
| xml_etree_process          | 37.7 ms                                                     | 41.2 ms: 1.09x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.50 sec: 1.10x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.81 ms: 1.10x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.51 ms: 1.10x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 17.9 ms: 1.10x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 64.9 ms: 1.10x slower                                                       |
| django_template            | 22.9 ms                                                     | 25.4 ms: 1.11x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.15 ms: 1.12x slower                                                       |
| fannkuch                   | 247 ms                                                      | 278 ms: 1.13x slower                                                        |
| coverage                   | 40.8 ms                                                     | 46.3 ms: 1.13x slower                                                       |
| richards_super             | 32.1 ms                                                     | 36.4 ms: 1.13x slower                                                       |
| richards                   | 28.4 ms                                                     | 32.5 ms: 1.14x slower                                                       |
| nbody                      | 71.9 ms                                                     | 82.8 ms: 1.15x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.58 sec: 1.16x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 91.2 ms: 1.16x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 933 us: 1.16x slower                                                        |
| pickle_pure_python         | 195 us                                                      | 227 us: 1.16x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.81 ms: 1.16x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 155 us: 1.17x slower                                                        |
| json_dumps                 | 5.70 ms                                                     | 6.66 ms: 1.17x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.18x slower                                                        |
| bench_mp_pool              | 69.2 ms                                                     | 82.0 ms: 1.19x slower                                                       |
| python_startup             | 19.5 ms                                                     | 24.0 ms: 1.24x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.91 ms: 1.25x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.38 ms: 1.84x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (2): json, chaos
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241116-3.14.0a1+-ed81971/bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.025x slower
# HPT report

- Reliability score: 99.54% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown