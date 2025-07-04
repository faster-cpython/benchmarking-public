# Results vs. 3.12.0

- fork: python
- ref: c419af9e277bea7dd78f
- machine: windows-amd64
- commit hash: c419af9
- commit date: 2025-06-28
- overall geometric mean: 1.111x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 221 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 393 ms: 1.96x faster                                                       |
| async_tree_io              | 731 ms                                                      | 397 ms: 1.84x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                       |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.70x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 169 ms: 1.69x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 209 ms: 1.62x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.68x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 53.5 ms: 1.34x faster                                                      |
| float          | 56.8 ms                                                     | 44.6 ms: 1.27x faster                                                      |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 79.8 ms: 1.10x faster                                                      |
| regex_dna      | 126 ms                                                      | 120 ms: 1.05x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.1 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 108 us: 1.23x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.14 sec: 1.19x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 50.2 ms: 1.11x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 34.6 ms: 1.09x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 90.4 ms: 1.03x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.5 ms: 1.03x faster                                                      |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.04x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 204 us: 1.05x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.28 ms: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                      |
| python_startup         | 19.5 ms                                                     | 26.1 ms: 1.34x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.54 ms: 1.28x faster                                                      |
| django_template | 22.9 ms                                                     | 24.1 ms: 1.05x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.10x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.6 ms: 2.55x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 393 ms: 1.96x faster                                                       |
| async_tree_io              | 731 ms                                                      | 397 ms: 1.84x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                       |
| mdp                        | 1.37 sec                                                    | 806 ms: 1.70x faster                                                       |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.70x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 169 ms: 1.69x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 209 ms: 1.62x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                       |
| deepcopy                   | 238 us                                                      | 173 us: 1.37x faster                                                       |
| nbody                      | 71.9 ms                                                     | 53.5 ms: 1.34x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.6 us: 1.33x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 18.1 us: 1.31x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.54 ms: 1.28x faster                                                      |
| float                      | 56.8 ms                                                     | 44.6 ms: 1.27x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 108 us: 1.23x faster                                                       |
| scimark_fft                | 184 ms                                                      | 152 ms: 1.21x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.14 sec: 1.19x faster                                                     |
| generators                 | 22.5 ms                                                     | 19.4 ms: 1.16x faster                                                      |
| go                         | 91.6 ms                                                     | 79.3 ms: 1.15x faster                                                      |
| pyflate                    | 295 ms                                                      | 257 ms: 1.15x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.83 us: 1.14x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 915 ms: 1.14x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.55 us: 1.14x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 453 ms: 1.13x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.27 ms: 1.12x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 50.2 ms: 1.11x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 54.8 ns: 1.10x faster                                                      |
| fannkuch                   | 247 ms                                                      | 224 ms: 1.10x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 79.8 ms: 1.10x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 34.6 ms: 1.09x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 41.0 ms: 1.08x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.5 ms: 1.05x faster                                                      |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.05x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.2 ms: 1.05x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 71.2 ms: 1.05x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 87.7 ms: 1.04x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 64.2 ms: 1.04x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 46.5 ms: 1.04x faster                                                      |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 60.3 ms: 1.04x faster                                                      |
| json                       | 3.05 ms                                                     | 2.94 ms: 1.04x faster                                                      |
| raytrace                   | 192 ms                                                      | 186 ms: 1.04x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 90.4 ms: 1.03x faster                                                      |
| richards_super             | 32.1 ms                                                     | 31.2 ms: 1.03x faster                                                      |
| richards                   | 28.4 ms                                                     | 27.7 ms: 1.03x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.5 ms: 1.03x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.56 us: 1.02x faster                                                      |
| sympy_str                  | 175 ms                                                      | 172 ms: 1.02x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.8 ms: 1.02x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.19 us: 1.01x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 14.1 ms: 1.01x faster                                                      |
| async_generators           | 239 ms                                                      | 242 ms: 1.01x slower                                                       |
| 2to3                       | 218 ms                                                      | 221 ms: 1.01x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.25 ms: 1.03x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.25 ms: 1.04x slower                                                      |
| sympy_expand               | 284 ms                                                      | 296 ms: 1.04x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.04x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 204 us: 1.05x slower                                                       |
| coroutines                 | 14.3 ms                                                     | 15.0 ms: 1.05x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.1 ms: 1.05x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.27 ms: 1.05x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 83.0 ms: 1.05x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 62.4 ms: 1.06x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.28 ms: 1.10x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 106 us: 1.11x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                      |
| coverage                   | 40.8 ms                                                     | 51.0 ms: 1.25x slower                                                      |
| python_startup             | 19.5 ms                                                     | 26.1 ms: 1.34x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.15 ms: 1.41x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.33 ms: 1.77x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                               |

Benchmark hidden because not significant (3): regex_effbot, pycparser, docutils
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250628-3.15.0a0-c419af9-JIT/bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.111x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown