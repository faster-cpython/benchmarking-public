# Results vs. 3.12.0

- fork: faster-cpython
- ref: explicit_check_perio
- machine: windows-amd64
- commit hash: c84beef
- commit date: 2025-06-23
- overall geometric mean: 1.058x faster
- HPT reliability: 93.51%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 226 ms: 1.03x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                         |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 418 ms: 1.84x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 424 ms: 1.72x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 226 ms: 1.63x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 183 ms: 1.56x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 188 ms: 1.55x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 228 ms: 1.49x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 351 ms: 1.43x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 345 ms: 1.42x faster                                                                 |
| Geometric mean             | (ref)                                                       | 1.58x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 46.1 ms: 1.23x faster                                                                |
| nbody          | 71.9 ms                                                     | 65.2 ms: 1.10x faster                                                                |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 121 ms: 1.04x faster                                                                 |
| regex_compile  | 87.5 ms                                                     | 84.1 ms: 1.04x faster                                                                |
| regex_v8       | 14.2 ms                                                     | 14.0 ms: 1.02x faster                                                                |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                                |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 88.2 ms: 1.05x faster                                                                |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.1 ms: 1.03x faster                                                                |
| xml_etree_generate   | 55.8 ms                                                     | 56.4 ms: 1.01x slower                                                                |
| tomli_loads          | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                               |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.04x slower                                                                |
| xml_etree_process    | 37.7 ms                                                     | 40.1 ms: 1.06x slower                                                                |
| unpickle_pure_python | 133 us                                                      | 142 us: 1.07x slower                                                                 |
| json_dumps           | 5.70 ms                                                     | 6.27 ms: 1.10x slower                                                                |
| pickle_pure_python   | 195 us                                                      | 222 us: 1.14x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                                |
| python_startup         | 19.5 ms                                                     | 26.0 ms: 1.34x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.78 ms: 1.04x faster                                                                |
| django_template | 22.9 ms                                                     | 25.1 ms: 1.09x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.6 ms: 2.54x faster                                                                |
| async_tree_io_tg           | 771 ms                                                      | 418 ms: 1.84x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 424 ms: 1.72x faster                                                                 |
| mdp                        | 1.37 sec                                                    | 835 ms: 1.64x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 226 ms: 1.63x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 183 ms: 1.56x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 188 ms: 1.55x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 228 ms: 1.49x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 351 ms: 1.43x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 345 ms: 1.42x faster                                                                 |
| deepcopy                   | 238 us                                                      | 178 us: 1.33x faster                                                                 |
| comprehensions             | 14.1 us                                                     | 11.0 us: 1.28x faster                                                                |
| deepcopy_memo              | 23.7 us                                                     | 18.9 us: 1.25x faster                                                                |
| float                      | 56.8 ms                                                     | 46.1 ms: 1.23x faster                                                                |
| go                         | 91.6 ms                                                     | 79.3 ms: 1.15x faster                                                                |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.11x faster                                                                |
| nbody                      | 71.9 ms                                                     | 65.2 ms: 1.10x faster                                                                |
| generators                 | 22.5 ms                                                     | 20.5 ms: 1.10x faster                                                                |
| deepcopy_reduce            | 2.09 us                                                     | 1.90 us: 1.10x faster                                                                |
| spectral_norm              | 66.9 ms                                                     | 62.1 ms: 1.08x faster                                                                |
| chaos                      | 43.3 ms                                                     | 41.0 ms: 1.06x faster                                                                |
| xml_etree_parse            | 93.0 ms                                                     | 88.2 ms: 1.05x faster                                                                |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.5 ms: 1.05x faster                                                                |
| scimark_sor                | 78.8 ms                                                     | 75.2 ms: 1.05x faster                                                                |
| dulwich_log                | 44.3 ms                                                     | 42.3 ms: 1.05x faster                                                                |
| mako                       | 7.09 ms                                                     | 6.78 ms: 1.04x faster                                                                |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.04x faster                                                                 |
| regex_compile              | 87.5 ms                                                     | 84.1 ms: 1.04x faster                                                                |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                                 |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.1 ms: 1.03x faster                                                                |
| regex_v8                   | 14.2 ms                                                     | 14.0 ms: 1.02x faster                                                                |
| raytrace                   | 192 ms                                                      | 189 ms: 1.02x faster                                                                 |
| async_generators           | 239 ms                                                      | 235 ms: 1.02x faster                                                                 |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                                |
| json                       | 3.05 ms                                                     | 3.01 ms: 1.01x faster                                                                |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.53 ms: 1.01x faster                                                                |
| sympy_sum                  | 91.5 ms                                                     | 90.8 ms: 1.01x faster                                                                |
| sympy_integrate            | 13.0 ms                                                     | 12.9 ms: 1.00x faster                                                                |
| sympy_str                  | 175 ms                                                      | 176 ms: 1.01x slower                                                                 |
| xml_etree_generate         | 55.8 ms                                                     | 56.4 ms: 1.01x slower                                                                |
| coroutines                 | 14.3 ms                                                     | 14.4 ms: 1.01x slower                                                                |
| richards_super             | 32.1 ms                                                     | 32.6 ms: 1.02x slower                                                                |
| scimark_lu                 | 58.9 ms                                                     | 60.1 ms: 1.02x slower                                                                |
| crypto_pyaes               | 48.5 ms                                                     | 49.8 ms: 1.03x slower                                                                |
| tomli_loads                | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                               |
| nqueens                    | 62.8 ms                                                     | 64.7 ms: 1.03x slower                                                                |
| 2to3                       | 218 ms                                                      | 226 ms: 1.03x slower                                                                 |
| hexiom                     | 4.10 ms                                                     | 4.25 ms: 1.04x slower                                                                |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.04x slower                                                                |
| deltablue                  | 2.16 ms                                                     | 2.24 ms: 1.04x slower                                                                |
| fannkuch                   | 247 ms                                                      | 259 ms: 1.05x slower                                                                 |
| logging_simple             | 6.28 us                                                     | 6.62 us: 1.05x slower                                                                |
| pycparser                  | 699 ms                                                      | 739 ms: 1.06x slower                                                                 |
| sympy_expand               | 284 ms                                                      | 302 ms: 1.06x slower                                                                 |
| logging_format             | 6.72 us                                                     | 7.14 us: 1.06x slower                                                                |
| xml_etree_process          | 37.7 ms                                                     | 40.1 ms: 1.06x slower                                                                |
| unpickle_pure_python       | 133 us                                                      | 142 us: 1.07x slower                                                                 |
| django_template            | 22.9 ms                                                     | 25.1 ms: 1.09x slower                                                                |
| json_dumps                 | 5.70 ms                                                     | 6.27 ms: 1.10x slower                                                                |
| pprint_safe_repr           | 513 ms                                                      | 566 ms: 1.10x slower                                                                 |
| telco                      | 4.13 ms                                                     | 4.60 ms: 1.11x slower                                                                |
| pprint_pformat             | 1.05 sec                                                    | 1.17 sec: 1.12x slower                                                               |
| typing_runtime_protocols   | 95.1 us                                                     | 107 us: 1.13x slower                                                                 |
| pickle_pure_python         | 195 us                                                      | 222 us: 1.14x slower                                                                 |
| python_startup_no_site     | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                                |
| coverage                   | 40.8 ms                                                     | 49.7 ms: 1.22x slower                                                                |
| python_startup             | 19.5 ms                                                     | 26.0 ms: 1.34x slower                                                                |
| gc_traversal               | 1.52 ms                                                     | 2.14 ms: 1.41x slower                                                                |
| create_gc_cycles           | 752 us                                                      | 1.33 ms: 1.77x slower                                                                |
| logging_silent             | 60.5 ns                                                     | 323 ns: 5.33x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                         |

Benchmark hidden because not significant (5): docutils, pyflate, scimark_fft, meteor_contest, richards
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250623-3.15.0a0-c84beef/bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.058x faster

# HPT report

- Reliability score: 93.51% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown