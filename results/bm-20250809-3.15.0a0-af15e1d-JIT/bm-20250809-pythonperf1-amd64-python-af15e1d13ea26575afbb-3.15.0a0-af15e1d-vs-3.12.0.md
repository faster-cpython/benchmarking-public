# Results vs. 3.12.0

- fork: python
- ref: af15e1d13ea26575afbb
- machine: windows-amd64
- commit hash: af15e1d
- commit date: 2025-08-09
- overall geometric mean: 1.124x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 223 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 387 ms: 1.99x faster                                                       |
| async_tree_io              | 731 ms                                                      | 389 ms: 1.88x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 167 ms: 1.71x faster                                                       |
| async_tree_none            | 291 ms                                                      | 174 ms: 1.68x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 205 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 337 ms: 1.49x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 332 ms: 1.47x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.69x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 52.8 ms: 1.36x faster                                                      |
| float          | 56.8 ms                                                     | 44.9 ms: 1.26x faster                                                      |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 77.7 ms: 1.13x faster                                                      |
| regex_dna      | 126 ms                                                      | 120 ms: 1.06x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.7 ms: 1.04x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 105 us: 1.27x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.09 sec: 1.25x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 51.1 ms: 1.09x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 87.9 ms: 1.06x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 35.7 ms: 1.06x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.39 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.2 ms: 1.03x faster                                                      |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.02x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 204 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.9 ms: 1.23x slower                                                      |
| python_startup         | 19.5 ms                                                     | 26.8 ms: 1.38x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.30x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.38 ms: 1.32x faster                                                      |
| django_template | 22.9 ms                                                     | 24.4 ms: 1.06x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.1 ms: 2.51x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 387 ms: 1.99x faster                                                       |
| async_tree_io              | 731 ms                                                      | 389 ms: 1.88x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                       |
| mdp                        | 1.37 sec                                                    | 800 ms: 1.72x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 167 ms: 1.71x faster                                                       |
| async_tree_none            | 291 ms                                                      | 174 ms: 1.68x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 205 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 337 ms: 1.49x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 332 ms: 1.47x faster                                                       |
| deepcopy                   | 238 us                                                      | 169 us: 1.41x faster                                                       |
| nbody                      | 71.9 ms                                                     | 52.8 ms: 1.36x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.6 us: 1.33x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.38 ms: 1.32x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 18.1 us: 1.31x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 105 us: 1.27x faster                                                       |
| float                      | 56.8 ms                                                     | 44.9 ms: 1.26x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.09 sec: 1.25x faster                                                     |
| scimark_fft                | 184 ms                                                      | 151 ms: 1.22x faster                                                       |
| go                         | 91.6 ms                                                     | 75.7 ms: 1.21x faster                                                      |
| fannkuch                   | 247 ms                                                      | 209 ms: 1.18x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 893 ms: 1.17x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 440 ms: 1.17x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.82 us: 1.15x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.7 ms: 1.14x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 77.7 ms: 1.13x faster                                                      |
| pyflate                    | 295 ms                                                      | 263 ms: 1.12x faster                                                       |
| raytrace                   | 192 ms                                                      | 174 ms: 1.10x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.33 ms: 1.10x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 51.1 ms: 1.09x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 55.3 ns: 1.09x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.61 us: 1.09x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 40.9 ms: 1.08x faster                                                      |
| chaos                      | 43.3 ms                                                     | 40.3 ms: 1.07x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 87.9 ms: 1.06x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 74.5 ms: 1.06x faster                                                      |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.06x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 35.7 ms: 1.06x faster                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.39 ms: 1.06x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.6 ms: 1.05x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 59.9 ms: 1.05x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 46.3 ms: 1.05x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 87.5 ms: 1.05x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.43 us: 1.04x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.8 ms: 1.04x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 71.6 ms: 1.04x faster                                                      |
| richards                   | 28.4 ms                                                     | 27.3 ms: 1.04x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.04 us: 1.04x faster                                                      |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 13.7 ms: 1.04x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.2 ms: 1.03x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 57.2 ms: 1.03x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.7 ms: 1.02x faster                                                      |
| sympy_str                  | 175 ms                                                      | 173 ms: 1.01x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 66.2 ms: 1.01x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 4.06 ms: 1.01x faster                                                      |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.02x slower                                                      |
| json                       | 3.05 ms                                                     | 3.10 ms: 1.02x slower                                                      |
| 2to3                       | 218 ms                                                      | 223 ms: 1.02x slower                                                       |
| sympy_expand               | 284 ms                                                      | 292 ms: 1.03x slower                                                       |
| coroutines                 | 14.3 ms                                                     | 14.7 ms: 1.03x slower                                                      |
| async_generators           | 239 ms                                                      | 250 ms: 1.04x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 204 us: 1.04x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.26 ms: 1.05x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.4 ms: 1.06x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 103 us: 1.08x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.75 ms: 1.15x slower                                                      |
| coverage                   | 40.8 ms                                                     | 48.5 ms: 1.19x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.9 ms: 1.23x slower                                                      |
| python_startup             | 19.5 ms                                                     | 26.8 ms: 1.38x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.14 ms: 1.41x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.33 ms: 1.77x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.12x faster                                                               |

Benchmark hidden because not significant (2): pycparser, docutils
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250809-3.15.0a0-af15e1d-JIT/bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.124x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown