# Results vs. 3.12.0

- fork: python
- ref: 09d6f5dc7824c74672ad
- machine: windows-amd64
- commit hash: 09d6f5d
- commit date: 2024-11-07
- overall geometric mean: 1.028x faster
- HPT reliability: 83.20%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 243 ms: 1.11x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.89 sec: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 250 ms: 1.47x faster                                                        |
| async_tree_none            | 291 ms                                                      | 204 ms: 1.43x faster                                                        |
| async_tree_io              | 731 ms                                                      | 517 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 204 ms: 1.40x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 574 ms: 1.34x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 253 ms: 1.34x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 396 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 395 ms: 1.24x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.36x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 56.3 ms: 1.28x faster                                                       |
| float          | 56.8 ms                                                     | 47.1 ms: 1.21x faster                                                       |
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.5 ms: 1.02x slower                                                       |
| regex_compile  | 87.5 ms                                                     | 91.2 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                     | 50.5 ms: 1.11x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.28 sec: 1.07x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 35.6 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.0 ms: 1.05x faster                                                       |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 207 us: 1.06x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.12 ms: 1.07x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 144 us: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.6 ms: 1.09x slower                                                       |
| python_startup         | 19.5 ms                                                     | 23.5 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.06 ms: 1.40x faster                                                       |
| django_template | 22.9 ms                                                     | 27.3 ms: 1.19x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.08x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 250 ms: 1.47x faster                                                        |
| async_tree_none            | 291 ms                                                      | 204 ms: 1.43x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 16.7 us: 1.42x faster                                                       |
| async_tree_io              | 731 ms                                                      | 517 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 204 ms: 1.40x faster                                                        |
| mako                       | 7.09 ms                                                     | 5.06 ms: 1.40x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 574 ms: 1.34x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 253 ms: 1.34x faster                                                        |
| nbody                      | 71.9 ms                                                     | 56.3 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 396 ms: 1.27x faster                                                        |
| deepcopy                   | 238 us                                                      | 191 us: 1.24x faster                                                        |
| scimark_sor                | 78.8 ms                                                     | 63.3 ms: 1.24x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 395 ms: 1.24x faster                                                        |
| spectral_norm              | 66.9 ms                                                     | 54.1 ms: 1.24x faster                                                       |
| float                      | 56.8 ms                                                     | 47.1 ms: 1.21x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 40.3 ms: 1.20x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.8 us: 1.20x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 37.0 ms: 1.18x faster                                                       |
| scimark_fft                | 184 ms                                                      | 157 ms: 1.18x faster                                                        |
| scimark_lu                 | 58.9 ms                                                     | 51.8 ms: 1.14x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.25 ms: 1.14x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 922 ms: 1.13x faster                                                        |
| pprint_safe_repr           | 513 ms                                                      | 455 ms: 1.13x faster                                                        |
| deepcopy_reduce            | 2.09 us                                                     | 1.87 us: 1.12x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 39.6 ms: 1.12x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.11x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 50.5 ms: 1.11x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 55.0 ns: 1.10x faster                                                       |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.28 sec: 1.07x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 75.2 ms: 1.07x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.4 ms: 1.06x faster                                                       |
| chaos                      | 43.3 ms                                                     | 40.9 ms: 1.06x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 35.6 ms: 1.06x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.0 ms: 1.05x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 819 us: 1.05x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                       |
| json                       | 3.05 ms                                                     | 2.93 ms: 1.04x faster                                                       |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| logging_format             | 6.72 us                                                     | 6.52 us: 1.03x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.11 us: 1.03x faster                                                       |
| fannkuch                   | 247 ms                                                      | 244 ms: 1.01x faster                                                        |
| go                         | 91.6 ms                                                     | 91.2 ms: 1.00x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 63.2 ms: 1.01x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 75.8 ms: 1.02x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.5 ms: 1.02x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                       |
| pyflate                    | 295 ms                                                      | 303 ms: 1.03x slower                                                        |
| pycparser                  | 699 ms                                                      | 720 ms: 1.03x slower                                                        |
| regex_compile              | 87.5 ms                                                     | 91.2 ms: 1.04x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 207 us: 1.06x slower                                                        |
| json_dumps                 | 5.70 ms                                                     | 6.12 ms: 1.07x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.46 ms: 1.08x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 144 us: 1.08x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 17.6 ms: 1.09x slower                                                       |
| sympy_str                  | 175 ms                                                      | 190 ms: 1.09x slower                                                        |
| deltablue                  | 2.16 ms                                                     | 2.35 ms: 1.09x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 888 us: 1.10x slower                                                        |
| sqlglot_normalize          | 187 ms                                                      | 207 ms: 1.11x slower                                                        |
| sympy_sum                  | 91.5 ms                                                     | 102 ms: 1.11x slower                                                        |
| raytrace                   | 192 ms                                                      | 214 ms: 1.11x slower                                                        |
| 2to3                       | 218 ms                                                      | 243 ms: 1.11x slower                                                        |
| async_generators           | 239 ms                                                      | 267 ms: 1.12x slower                                                        |
| mdp                        | 1.37 sec                                                    | 1.54 sec: 1.12x slower                                                      |
| coverage                   | 40.8 ms                                                     | 46.1 ms: 1.13x slower                                                       |
| sympy_expand               | 284 ms                                                      | 323 ms: 1.14x slower                                                        |
| docutils                   | 1.66 sec                                                    | 1.89 sec: 1.14x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.18 ms: 1.16x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 113 us: 1.18x slower                                                        |
| django_template            | 22.9 ms                                                     | 27.3 ms: 1.19x slower                                                       |
| richards_super             | 32.1 ms                                                     | 38.6 ms: 1.20x slower                                                       |
| python_startup             | 19.5 ms                                                     | 23.5 ms: 1.21x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 15.7 ms: 1.21x slower                                                       |
| richards                   | 28.4 ms                                                     | 34.5 ms: 1.22x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 42.5 ms: 1.23x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 87.1 ms: 1.26x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.92 ms: 1.26x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 5.20 ms: 1.27x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.37 ms: 1.83x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_parse, generators
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241107-3.14.0a1+-09d6f5d-JIT/bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.028x faster
# HPT report

- Reliability score: 83.20% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown