# Results vs. 3.10.4

- fork: python
- ref: 328187cc4fcdd578db42
- machine: linux-x86_64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.037x slower
- HPT reliability: 99.64%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.52x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 401 ms: 1.14x slower                                                         |
| docutils       | 3.41 sec                                                     | 3.27 sec: 1.04x faster                                                       |
| html5lib       | 94.6 ms                                                      | 101 ms: 1.06x slower                                                         |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 902 ms: 1.77x faster                                                         |
| async_tree_none         | 692 ms                                                       | 400 ms: 1.73x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 500 ms: 1.64x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 666 ms: 1.41x faster                                                         |
| Geometric mean          | (ref)                                                        | 1.63x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 271 ms                                                       | 247 ms: 1.10x faster                                                         |
| nbody          | 134 ms                                                       | 141 ms: 1.05x slower                                                         |
| float          | 111 ms                                                       | 133 ms: 1.20x slower                                                         |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 261 ms                                                       | 243 ms: 1.07x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 27.7 ms: 1.02x slower                                                        |
| regex_compile  | 190 ms                                                       | 198 ms: 1.04x slower                                                         |
| regex_effbot   | 3.09 ms                                                      | 3.32 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 160 ms                                                       | 136 ms: 1.18x faster                                                         |
| json_loads           | 30.3 us                                                      | 27.9 us: 1.09x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 102 ms: 1.08x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 14.8 ms: 1.02x slower                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.98 sec: 1.02x slower                                                       |
| xml_etree_process    | 75.9 ms                                                      | 83.5 ms: 1.10x slower                                                        |
| unpickle_pure_python | 312 us                                                       | 348 us: 1.12x slower                                                         |
| xml_etree_generate   | 92.3 ms                                                      | 104 ms: 1.13x slower                                                         |
| pickle_pure_python   | 455 us                                                       | 538 us: 1.18x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 12.2 ms: 1.66x slower                                                        |
| python_startup         | 11.5 ms                                                      | 20.0 ms: 1.74x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.70x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 55.9 ms: 1.11x slower                                                        |
| genshi_xml      | 63.3 ms                                                      | 72.5 ms: 1.15x slower                                                        |
| genshi_text     | 31.4 ms                                                      | 37.7 ms: 1.20x slower                                                        |
| mako            | 14.7 ms                                                      | 21.0 ms: 1.43x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.22x slower                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 234 us: 2.29x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 902 ms: 1.77x faster                                                         |
| async_tree_none          | 692 ms                                                       | 400 ms: 1.73x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 500 ms: 1.64x faster                                                         |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 666 ms: 1.41x faster                                                         |
| generators               | 57.3 ms                                                      | 41.1 ms: 1.40x faster                                                        |
| pylint                   | 566 ms                                                       | 412 ms: 1.37x faster                                                         |
| deepcopy                 | 468 us                                                       | 371 us: 1.26x faster                                                         |
| coroutines               | 30.3 ms                                                      | 25.2 ms: 1.20x faster                                                        |
| spectral_norm            | 139 ms                                                       | 117 ms: 1.19x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 136 ms: 1.18x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 42.6 us: 1.17x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 18.3 ms: 1.16x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 108 ms: 1.11x faster                                                         |
| pidigits                 | 271 ms                                                       | 247 ms: 1.10x faster                                                         |
| json_loads               | 30.3 us                                                      | 27.9 us: 1.09x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 102 ms: 1.08x faster                                                         |
| regex_dna                | 261 ms                                                       | 243 ms: 1.07x faster                                                         |
| docutils                 | 3.41 sec                                                     | 3.27 sec: 1.04x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.88 us: 1.04x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 380 ms: 1.03x faster                                                         |
| json                     | 5.86 ms                                                      | 5.74 ms: 1.02x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.65 sec: 1.02x faster                                                       |
| pyflate                  | 733 ms                                                       | 728 ms: 1.01x faster                                                         |
| mdp                      | 3.01 sec                                                     | 3.03 sec: 1.01x slower                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 4.06 us: 1.01x slower                                                        |
| json_dumps               | 14.5 ms                                                      | 14.8 ms: 1.02x slower                                                        |
| regex_v8                 | 27.2 ms                                                      | 27.7 ms: 1.02x slower                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.98 sec: 1.02x slower                                                       |
| richards_super           | 90.6 ms                                                      | 92.7 ms: 1.02x slower                                                        |
| chaos                    | 109 ms                                                       | 111 ms: 1.03x slower                                                         |
| nqueens                  | 115 ms                                                       | 119 ms: 1.04x slower                                                         |
| regex_compile            | 190 ms                                                       | 198 ms: 1.04x slower                                                         |
| scimark_lu               | 167 ms                                                       | 174 ms: 1.04x slower                                                         |
| go                       | 262 ms                                                       | 276 ms: 1.05x slower                                                         |
| nbody                    | 134 ms                                                       | 141 ms: 1.05x slower                                                         |
| richards                 | 75.1 ms                                                      | 79.3 ms: 1.06x slower                                                        |
| deltablue                | 7.50 ms                                                      | 7.92 ms: 1.06x slower                                                        |
| sqlalchemy_imperative    | 22.7 ms                                                      | 24.1 ms: 1.06x slower                                                        |
| dulwich_log              | 81.1 ms                                                      | 86.1 ms: 1.06x slower                                                        |
| html5lib                 | 94.6 ms                                                      | 101 ms: 1.06x slower                                                         |
| regex_effbot             | 3.09 ms                                                      | 3.32 ms: 1.07x slower                                                        |
| logging_silent           | 167 ns                                                       | 181 ns: 1.08x slower                                                         |
| thrift                   | 1.18 ms                                                      | 1.28 ms: 1.09x slower                                                        |
| comprehensions           | 26.7 us                                                      | 29.2 us: 1.09x slower                                                        |
| sympy_integrate          | 28.2 ms                                                      | 30.9 ms: 1.10x slower                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 1.15 sec: 1.10x slower                                                       |
| xml_etree_process        | 75.9 ms                                                      | 83.5 ms: 1.10x slower                                                        |
| sqlglot_normalize        | 144 ms                                                       | 159 ms: 1.11x slower                                                         |
| pprint_pformat           | 2.15 sec                                                     | 2.39 sec: 1.11x slower                                                       |
| django_template          | 50.2 ms                                                      | 55.9 ms: 1.11x slower                                                        |
| fannkuch                 | 483 ms                                                       | 538 ms: 1.11x slower                                                         |
| unpickle_pure_python     | 312 us                                                       | 348 us: 1.12x slower                                                         |
| gc_traversal             | 3.42 ms                                                      | 3.82 ms: 1.12x slower                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 78.8 ms: 1.12x slower                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 104 ms: 1.13x slower                                                         |
| hexiom                   | 9.42 ms                                                      | 10.7 ms: 1.14x slower                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.80 ms: 1.14x slower                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 217 ms: 1.14x slower                                                         |
| 2to3                     | 350 ms                                                       | 401 ms: 1.14x slower                                                         |
| genshi_xml               | 63.3 ms                                                      | 72.5 ms: 1.15x slower                                                        |
| meteor_contest           | 138 ms                                                       | 159 ms: 1.15x slower                                                         |
| sympy_str                | 360 ms                                                       | 414 ms: 1.15x slower                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 124 ms: 1.15x slower                                                         |
| raytrace                 | 489 ms                                                       | 565 ms: 1.16x slower                                                         |
| pickle_pure_python       | 455 us                                                       | 538 us: 1.18x slower                                                         |
| logging_simple           | 8.88 us                                                      | 10.5 us: 1.19x slower                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 3.18 ms: 1.19x slower                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 2.66 ms: 1.19x slower                                                        |
| logging_format           | 9.64 us                                                      | 11.5 us: 1.19x slower                                                        |
| float                    | 111 ms                                                       | 133 ms: 1.20x slower                                                         |
| genshi_text              | 31.4 ms                                                      | 37.7 ms: 1.20x slower                                                        |
| sympy_expand             | 600 ms                                                       | 758 ms: 1.26x slower                                                         |
| scimark_sor              | 180 ms                                                       | 229 ms: 1.27x slower                                                         |
| sympy_sum                | 193 ms                                                       | 247 ms: 1.28x slower                                                         |
| async_generators         | 421 ms                                                       | 556 ms: 1.32x slower                                                         |
| telco                    | 7.23 ms                                                      | 9.63 ms: 1.33x slower                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 1.55 ms: 1.36x slower                                                        |
| mako                     | 14.7 ms                                                      | 21.0 ms: 1.43x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.71 ms: 1.54x slower                                                        |
| coverage                 | 63.3 ms                                                      | 105 ms: 1.65x slower                                                         |
| python_startup_no_site   | 7.33 ms                                                      | 12.2 ms: 1.66x slower                                                        |
| python_startup           | 11.5 ms                                                      | 20.0 ms: 1.74x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 54.6 ms: 8.56x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.07x slower                                                                 |

Benchmark hidden because not significant (1): scimark_fft
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241130-3.14.0a2+-328187c-NOGIL/bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.037x slower

# HPT report

- Reliability score: 99.64% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.52x