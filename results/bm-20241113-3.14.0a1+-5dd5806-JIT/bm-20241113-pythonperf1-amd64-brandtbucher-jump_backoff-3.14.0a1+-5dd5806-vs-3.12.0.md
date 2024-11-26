# Results vs. 3.12.0

- fork: brandtbucher
- ref: jump_backoff
- machine: windows-amd64
- commit hash: 5dd5806
- commit date: 2024-11-13
- overall geometric mean: 1.030x faster
- HPT reliability: 90.36%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 229 ms: 1.05x slower                                                      |
| docutils       | 1.66 sec                                                    | 1.84 sec: 1.11x slower                                                    |
| Geometric mean | (ref)                                                       | 1.08x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 258 ms: 1.42x faster                                                      |
| async_tree_none_tg         | 285 ms                                                      | 205 ms: 1.39x faster                                                      |
| async_tree_none            | 291 ms                                                      | 214 ms: 1.36x faster                                                      |
| async_tree_io              | 731 ms                                                      | 544 ms: 1.34x faster                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 386 ms: 1.27x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 400 ms: 1.26x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 626 ms: 1.23x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 276 ms: 1.23x faster                                                      |
| Geometric mean             | (ref)                                                       | 1.31x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 56.7 ms: 1.27x faster                                                     |
| float          | 56.8 ms                                                     | 47.4 ms: 1.20x faster                                                     |
| pidigits       | 152 ms                                                      | 147 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 121 ms: 1.04x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                     |
| regex_v8       | 14.2 ms                                                     | 15.7 ms: 1.10x slower                                                     |
| Geometric mean | (ref)                                                       | 1.01x slower                                                              |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 109 us: 1.22x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 49.7 ms: 1.12x faster                                                     |
| tomli_loads          | 1.37 sec                                                    | 1.26 sec: 1.08x faster                                                    |
| xml_etree_process    | 37.7 ms                                                     | 35.5 ms: 1.06x faster                                                     |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.3 ms: 1.05x faster                                                     |
| json_loads           | 13.9 us                                                     | 14.7 us: 1.05x slower                                                     |
| pickle_pure_python   | 195 us                                                      | 208 us: 1.07x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.20 ms: 1.09x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                              |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                                     |
| python_startup         | 19.5 ms                                                     | 24.0 ms: 1.23x slower                                                     |
| Geometric mean         | (ref)                                                       | 1.17x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.12 ms: 1.38x faster                                                     |
| django_template | 22.9 ms                                                     | 26.6 ms: 1.16x slower                                                     |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 258 ms: 1.42x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 16.8 us: 1.41x faster                                                     |
| async_tree_none_tg         | 285 ms                                                      | 205 ms: 1.39x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.12 ms: 1.38x faster                                                     |
| async_tree_none            | 291 ms                                                      | 214 ms: 1.36x faster                                                      |
| async_tree_io              | 731 ms                                                      | 544 ms: 1.34x faster                                                      |
| nbody                      | 71.9 ms                                                     | 56.7 ms: 1.27x faster                                                     |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 386 ms: 1.27x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 400 ms: 1.26x faster                                                      |
| deepcopy                   | 238 us                                                      | 192 us: 1.24x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 63.5 ms: 1.24x faster                                                     |
| async_tree_io_tg           | 771 ms                                                      | 626 ms: 1.23x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 276 ms: 1.23x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 109 us: 1.22x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 39.9 ms: 1.22x faster                                                     |
| spectral_norm              | 66.9 ms                                                     | 55.7 ms: 1.20x faster                                                     |
| float                      | 56.8 ms                                                     | 47.4 ms: 1.20x faster                                                     |
| scimark_monte_carlo        | 43.7 ms                                                     | 36.7 ms: 1.19x faster                                                     |
| scimark_fft                | 184 ms                                                      | 156 ms: 1.18x faster                                                      |
| comprehensions             | 14.1 us                                                     | 12.0 us: 1.18x faster                                                     |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.21 ms: 1.16x faster                                                     |
| xml_etree_generate         | 55.8 ms                                                     | 49.7 ms: 1.12x faster                                                     |
| deepcopy_reduce            | 2.09 us                                                     | 1.87 us: 1.12x faster                                                     |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.11x faster                                                     |
| pprint_pformat             | 1.05 sec                                                    | 944 ms: 1.11x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 53.3 ms: 1.10x faster                                                     |
| pprint_safe_repr           | 513 ms                                                      | 467 ms: 1.10x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 40.4 ms: 1.10x faster                                                     |
| tomli_loads                | 1.37 sec                                                    | 1.26 sec: 1.08x faster                                                    |
| chaos                      | 43.3 ms                                                     | 40.4 ms: 1.07x faster                                                     |
| pathlib                    | 80.5 ms                                                     | 75.0 ms: 1.07x faster                                                     |
| xml_etree_process          | 37.7 ms                                                     | 35.5 ms: 1.06x faster                                                     |
| bench_thread_pool          | 857 us                                                      | 807 us: 1.06x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.5 ms: 1.05x faster                                                     |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.3 ms: 1.05x faster                                                     |
| logging_silent             | 60.5 ns                                                     | 57.9 ns: 1.05x faster                                                     |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.04x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 71.8 ms: 1.04x faster                                                     |
| pidigits                   | 152 ms                                                      | 147 ms: 1.03x faster                                                      |
| json                       | 3.05 ms                                                     | 2.99 ms: 1.02x faster                                                     |
| regex_effbot               | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                     |
| generators                 | 22.5 ms                                                     | 22.3 ms: 1.01x faster                                                     |
| pycparser                  | 699 ms                                                      | 693 ms: 1.01x faster                                                      |
| go                         | 91.6 ms                                                     | 93.1 ms: 1.02x slower                                                     |
| nqueens                    | 62.8 ms                                                     | 64.1 ms: 1.02x slower                                                     |
| telco                      | 4.13 ms                                                     | 4.25 ms: 1.03x slower                                                     |
| sympy_sum                  | 91.5 ms                                                     | 94.9 ms: 1.04x slower                                                     |
| fannkuch                   | 247 ms                                                      | 258 ms: 1.05x slower                                                      |
| sympy_str                  | 175 ms                                                      | 184 ms: 1.05x slower                                                      |
| 2to3                       | 218 ms                                                      | 229 ms: 1.05x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.7 us: 1.05x slower                                                     |
| pickle_pure_python         | 195 us                                                      | 208 us: 1.07x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 13.9 ms: 1.07x slower                                                     |
| deltablue                  | 2.16 ms                                                     | 2.34 ms: 1.08x slower                                                     |
| json_dumps                 | 5.70 ms                                                     | 6.20 ms: 1.09x slower                                                     |
| sqlglot_parse              | 804 us                                                      | 878 us: 1.09x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 15.7 ms: 1.10x slower                                                     |
| sqlglot_transpile          | 1.02 ms                                                     | 1.13 ms: 1.10x slower                                                     |
| python_startup_no_site     | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                                     |
| docutils                   | 1.66 sec                                                    | 1.84 sec: 1.11x slower                                                    |
| sqlglot_normalize          | 187 ms                                                      | 208 ms: 1.11x slower                                                      |
| raytrace                   | 192 ms                                                      | 214 ms: 1.11x slower                                                      |
| async_generators           | 239 ms                                                      | 268 ms: 1.12x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 38.7 ms: 1.12x slower                                                     |
| sympy_expand               | 284 ms                                                      | 320 ms: 1.13x slower                                                      |
| django_template            | 22.9 ms                                                     | 26.6 ms: 1.16x slower                                                     |
| richards_super             | 32.1 ms                                                     | 37.7 ms: 1.18x slower                                                     |
| mdp                        | 1.37 sec                                                    | 1.63 sec: 1.18x slower                                                    |
| coverage                   | 40.8 ms                                                     | 48.7 ms: 1.19x slower                                                     |
| richards                   | 28.4 ms                                                     | 33.9 ms: 1.19x slower                                                     |
| typing_runtime_protocols   | 95.1 us                                                     | 114 us: 1.20x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 5.05 ms: 1.23x slower                                                     |
| python_startup             | 19.5 ms                                                     | 24.0 ms: 1.23x slower                                                     |
| bench_mp_pool              | 69.2 ms                                                     | 86.6 ms: 1.25x slower                                                     |
| gc_traversal               | 1.52 ms                                                     | 1.92 ms: 1.26x slower                                                     |
| create_gc_cycles           | 752 us                                                      | 1.37 ms: 1.82x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                              |

Benchmark hidden because not significant (5): logging_format, logging_simple, regex_compile, xml_etree_parse, pyflate
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241113-3.14.0a1+-5dd5806-JIT/bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.030x faster
# HPT report

- Reliability score: 90.36% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown