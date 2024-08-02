# Results vs. 3.13.0b2

- fork: Fidget-Spinner
- ref: stackref_all
- machine: linux-x86_64
- commit hash: 144a6fa
- commit date: 2024-05-11
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 283 ms: 1.03x slower                                                    |
| chameleon      | 7.22 ms                                                    | 7.80 ms: 1.08x slower                                                   |
| docutils       | 2.83 sec                                                   | 2.89 sec: 1.02x slower                                                  |
| html5lib       | 67.2 ms                                                    | 69.6 ms: 1.03x slower                                                   |
| tornado_http   | 94.6 ms                                                    | 97.8 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                      | 1.04x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|---------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed   | 611 ms                                                     | 636 ms: 1.04x slower                                                    |
| async_tree_memoization_tg | 444 ms                                                     | 476 ms: 1.07x slower                                                    |
| async_tree_memoization    | 463 ms                                                     | 499 ms: 1.08x slower                                                    |
| async_tree_none_tg        | 336 ms                                                     | 362 ms: 1.08x slower                                                    |
| async_tree_io_tg          | 936 ms                                                     | 1.01 sec: 1.08x slower                                                  |
| Geometric mean            | (ref)                                                      | 1.05x slower                                                            |

Benchmark hidden because not significant (3): async_tree_none, async_tree_io, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 190 ms: 1.01x faster                                                    |
| float          | 78.9 ms                                                    | 86.7 ms: 1.10x slower                                                   |
| nbody          | 88.3 ms                                                    | 105 ms: 1.19x slower                                                    |
| Geometric mean | (ref)                                                      | 1.09x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                   |
| regex_dna      | 221 ms                                                     | 217 ms: 1.02x faster                                                    |
| regex_effbot   | 3.67 ms                                                    | 3.60 ms: 1.02x faster                                                   |
| regex_compile  | 137 ms                                                     | 144 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                      | 1.00x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_dict          | 34.8 us                                                    | 33.9 us: 1.02x faster                                                   |
| json_loads           | 28.9 us                                                    | 29.1 us: 1.01x slower                                                   |
| json_dumps           | 10.7 ms                                                    | 10.8 ms: 1.01x slower                                                   |
| pickle               | 11.5 us                                                    | 11.7 us: 1.02x slower                                                   |
| unpickle_list        | 5.34 us                                                    | 5.55 us: 1.04x slower                                                   |
| xml_etree_iterparse  | 107 ms                                                     | 112 ms: 1.04x slower                                                    |
| pickle_list          | 5.11 us                                                    | 5.41 us: 1.06x slower                                                   |
| xml_etree_process    | 61.2 ms                                                    | 65.1 ms: 1.06x slower                                                   |
| xml_etree_generate   | 87.4 ms                                                    | 93.4 ms: 1.07x slower                                                   |
| pickle_pure_python   | 305 us                                                     | 335 us: 1.10x slower                                                    |
| tomli_loads          | 2.12 sec                                                   | 2.34 sec: 1.10x slower                                                  |
| unpickle_pure_python | 218 us                                                     | 243 us: 1.12x slower                                                    |
| Geometric mean       | (ref)                                                      | 1.04x slower                                                            |

Benchmark hidden because not significant (2): unpickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                   |
| python_startup_no_site | 7.11 ms                                                    | 7.16 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 24.8 ms: 1.05x slower                                                   |
| genshi_xml      | 51.6 ms                                                    | 55.7 ms: 1.08x slower                                                   |
| django_template | 34.8 ms                                                    | 38.2 ms: 1.10x slower                                                   |
| mako            | 11.2 ms                                                    | 12.7 ms: 1.13x slower                                                   |
| Geometric mean  | (ref)                                                      | 1.09x slower                                                            |

All benchmarks:
===============

| Benchmark                 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|---------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                       | 2.79 sec                                                   | 2.66 sec: 1.05x faster                                                  |
| gc_traversal              | 3.98 ms                                                    | 3.81 ms: 1.04x faster                                                   |
| regex_v8                  | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                   |
| pickle_dict               | 34.8 us                                                    | 33.9 us: 1.02x faster                                                   |
| python_startup            | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                   |
| regex_dna                 | 221 ms                                                     | 217 ms: 1.02x faster                                                    |
| regex_effbot              | 3.67 ms                                                    | 3.60 ms: 1.02x faster                                                   |
| pidigits                  | 191 ms                                                     | 190 ms: 1.01x faster                                                    |
| sqlite_synth              | 2.99 us                                                    | 2.97 us: 1.01x faster                                                   |
| create_gc_cycles          | 1.82 ms                                                    | 1.80 ms: 1.01x faster                                                   |
| richards                  | 50.9 ms                                                    | 51.2 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl           | 1.84 sec                                                   | 1.85 sec: 1.01x slower                                                  |
| python_startup_no_site    | 7.11 ms                                                    | 7.16 ms: 1.01x slower                                                   |
| json_loads                | 28.9 us                                                    | 29.1 us: 1.01x slower                                                   |
| json_dumps                | 10.7 ms                                                    | 10.8 ms: 1.01x slower                                                   |
| crypto_pyaes              | 77.5 ms                                                    | 78.1 ms: 1.01x slower                                                   |
| asyncio_tcp               | 508 ms                                                     | 516 ms: 1.02x slower                                                    |
| dulwich_log               | 67.2 ms                                                    | 68.3 ms: 1.02x slower                                                   |
| pickle                    | 11.5 us                                                    | 11.7 us: 1.02x slower                                                   |
| richards_super            | 57.4 ms                                                    | 58.5 ms: 1.02x slower                                                   |
| docutils                  | 2.83 sec                                                   | 2.89 sec: 1.02x slower                                                  |
| scimark_lu                | 122 ms                                                     | 125 ms: 1.03x slower                                                    |
| flaskblogging             | 9.01 ms                                                    | 9.25 ms: 1.03x slower                                                   |
| dask                      | 369 ms                                                     | 380 ms: 1.03x slower                                                    |
| sympy_str                 | 282 ms                                                     | 291 ms: 1.03x slower                                                    |
| pathlib                   | 17.3 ms                                                    | 17.9 ms: 1.03x slower                                                   |
| 2to3                      | 274 ms                                                     | 283 ms: 1.03x slower                                                    |
| tornado_http              | 94.6 ms                                                    | 97.8 ms: 1.03x slower                                                   |
| html5lib                  | 67.2 ms                                                    | 69.6 ms: 1.03x slower                                                   |
| sympy_sum                 | 156 ms                                                     | 161 ms: 1.04x slower                                                    |
| sympy_integrate           | 20.5 ms                                                    | 21.2 ms: 1.04x slower                                                   |
| async_generators          | 442 ms                                                     | 458 ms: 1.04x slower                                                    |
| bench_thread_pool         | 834 us                                                     | 865 us: 1.04x slower                                                    |
| sympy_expand              | 473 ms                                                     | 491 ms: 1.04x slower                                                    |
| unpickle_list             | 5.34 us                                                    | 5.55 us: 1.04x slower                                                   |
| xml_etree_iterparse       | 107 ms                                                     | 112 ms: 1.04x slower                                                    |
| logging_format            | 6.47 us                                                    | 6.72 us: 1.04x slower                                                   |
| thrift                    | 823 us                                                     | 856 us: 1.04x slower                                                    |
| async_tree_cpu_io_mixed   | 611 ms                                                     | 636 ms: 1.04x slower                                                    |
| spectral_norm             | 116 ms                                                     | 121 ms: 1.04x slower                                                    |
| sqlglot_optimize          | 55.5 ms                                                    | 58.1 ms: 1.05x slower                                                   |
| genshi_text               | 23.7 ms                                                    | 24.8 ms: 1.05x slower                                                   |
| sqlglot_normalize         | 110 ms                                                     | 116 ms: 1.05x slower                                                    |
| json                      | 5.31 ms                                                    | 5.57 ms: 1.05x slower                                                   |
| meteor_contest            | 110 ms                                                     | 115 ms: 1.05x slower                                                    |
| regex_compile             | 137 ms                                                     | 144 ms: 1.05x slower                                                    |
| scimark_fft               | 392 ms                                                     | 414 ms: 1.05x slower                                                    |
| logging_simple            | 5.74 us                                                    | 6.06 us: 1.05x slower                                                   |
| pyflate                   | 484 ms                                                     | 512 ms: 1.06x slower                                                    |
| generators                | 29.6 ms                                                    | 31.3 ms: 1.06x slower                                                   |
| pickle_list               | 5.11 us                                                    | 5.41 us: 1.06x slower                                                   |
| xml_etree_process         | 61.2 ms                                                    | 65.1 ms: 1.06x slower                                                   |
| xml_etree_generate        | 87.4 ms                                                    | 93.4 ms: 1.07x slower                                                   |
| logging_silent            | 105 ns                                                     | 112 ns: 1.07x slower                                                    |
| async_tree_memoization_tg | 444 ms                                                     | 476 ms: 1.07x slower                                                    |
| deepcopy_reduce           | 3.35 us                                                    | 3.60 us: 1.08x slower                                                   |
| async_tree_memoization    | 463 ms                                                     | 499 ms: 1.08x slower                                                    |
| async_tree_none_tg        | 336 ms                                                     | 362 ms: 1.08x slower                                                    |
| sqlglot_transpile         | 1.63 ms                                                    | 1.76 ms: 1.08x slower                                                   |
| genshi_xml                | 51.6 ms                                                    | 55.7 ms: 1.08x slower                                                   |
| chameleon                 | 7.22 ms                                                    | 7.80 ms: 1.08x slower                                                   |
| async_tree_io_tg          | 936 ms                                                     | 1.01 sec: 1.08x slower                                                  |
| raytrace                  | 267 ms                                                     | 289 ms: 1.08x slower                                                    |
| hexiom                    | 6.30 ms                                                    | 6.82 ms: 1.08x slower                                                   |
| typing_runtime_protocols  | 165 us                                                     | 178 us: 1.08x slower                                                    |
| scimark_sparse_mat_mult   | 5.27 ms                                                    | 5.72 ms: 1.09x slower                                                   |
| pycparser                 | 1.16 sec                                                   | 1.26 sec: 1.09x slower                                                  |
| sqlglot_parse             | 1.32 ms                                                    | 1.43 ms: 1.09x slower                                                   |
| chaos                     | 61.3 ms                                                    | 66.8 ms: 1.09x slower                                                   |
| go                        | 145 ms                                                     | 158 ms: 1.09x slower                                                    |
| deepcopy                  | 367 us                                                     | 401 us: 1.09x slower                                                    |
| nqueens                   | 81.4 ms                                                    | 89.1 ms: 1.09x slower                                                   |
| pickle_pure_python        | 305 us                                                     | 335 us: 1.10x slower                                                    |
| django_template           | 34.8 ms                                                    | 38.2 ms: 1.10x slower                                                   |
| float                     | 78.9 ms                                                    | 86.7 ms: 1.10x slower                                                   |
| tomli_loads               | 2.12 sec                                                   | 2.34 sec: 1.10x slower                                                  |
| coroutines                | 23.2 ms                                                    | 25.5 ms: 1.10x slower                                                   |
| scimark_sor               | 127 ms                                                     | 141 ms: 1.10x slower                                                    |
| deltablue                 | 3.25 ms                                                    | 3.60 ms: 1.11x slower                                                   |
| scimark_monte_carlo       | 69.2 ms                                                    | 76.7 ms: 1.11x slower                                                   |
| unpickle_pure_python      | 218 us                                                     | 243 us: 1.12x slower                                                    |
| fannkuch                  | 402 ms                                                     | 449 ms: 1.12x slower                                                    |
| pprint_pformat            | 1.56 sec                                                   | 1.74 sec: 1.12x slower                                                  |
| pprint_safe_repr          | 758 ms                                                     | 853 ms: 1.12x slower                                                    |
| mako                      | 11.2 ms                                                    | 12.7 ms: 1.13x slower                                                   |
| deepcopy_memo             | 39.7 us                                                    | 45.1 us: 1.14x slower                                                   |
| comprehensions            | 16.6 us                                                    | 19.0 us: 1.14x slower                                                   |
| nbody                     | 88.3 ms                                                    | 105 ms: 1.19x slower                                                    |
| telco                     | 8.41 ms                                                    | 185 ms: 21.95x slower                                                   |
| Geometric mean            | (ref)                                                      | 1.08x slower                                                            |

Benchmark hidden because not significant (9): coverage, asyncio_websockets, bench_mp_pool, unpickle, xml_etree_parse, async_tree_none, async_tree_io, async_tree_cpu_io_mixed_tg, pylint
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, djangocms, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.00x