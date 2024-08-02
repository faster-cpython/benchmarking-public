# Results vs. base

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-x86_64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.01x slower
- HPT reliability: 89.55%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                                                                                | 305 ms: 1.06x slower                                                                                                      |
| chameleon      | 7.50 ms                                                                                                               | 7.68 ms: 1.02x slower                                                                                                     |
| docutils       | 2.97 sec                                                                                                              | 3.13 sec: 1.05x slower                                                                                                    |
| html5lib       | 73.3 ms                                                                                                               | 74.3 ms: 1.01x slower                                                                                                     |
| tornado_http   | 119 ms                                                                                                                | 124 ms: 1.04x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.04x slower                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_tree_memoization | 483 ms                                                                                                                | 470 ms: 1.03x faster                                                                                                      |
| async_tree_io_tg       | 917 ms                                                                                                                | 906 ms: 1.01x faster                                                                                                      |
| Geometric mean         | (ref)                                                                                                                 | 1.01x faster                                                                                                              |

Benchmark hidden because not significant (6): async_tree_none, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 88.7 ms                                                                                                               | 81.6 ms: 1.09x faster                                                                                                     |
| float          | 79.9 ms                                                                                                               | 74.2 ms: 1.08x faster                                                                                                     |
| pidigits       | 253 ms                                                                                                                | 250 ms: 1.01x faster                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.06x faster                                                                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                                                                                | 138 ms: 1.05x faster                                                                                                      |
| regex_dna      | 245 ms                                                                                                                | 243 ms: 1.01x faster                                                                                                      |
| regex_v8       | 25.1 ms                                                                                                               | 26.0 ms: 1.03x slower                                                                                                     |
| regex_effbot   | 3.46 ms                                                                                                               | 3.67 ms: 1.06x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                 | 1.01x slower                                                                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 2.48 sec                                                                                                              | 2.12 sec: 1.17x faster                                                                                                    |
| xml_etree_generate   | 86.4 ms                                                                                                               | 81.8 ms: 1.06x faster                                                                                                     |
| xml_etree_process    | 60.8 ms                                                                                                               | 58.0 ms: 1.05x faster                                                                                                     |
| xml_etree_iterparse  | 103 ms                                                                                                                | 101 ms: 1.02x faster                                                                                                      |
| json_dumps           | 10.8 ms                                                                                                               | 10.6 ms: 1.02x faster                                                                                                     |
| unpickle             | 15.5 us                                                                                                               | 15.4 us: 1.01x faster                                                                                                     |
| pickle_pure_python   | 316 us                                                                                                                | 318 us: 1.01x slower                                                                                                      |
| unpickle_list        | 4.73 us                                                                                                               | 4.79 us: 1.01x slower                                                                                                     |
| pickle_list          | 4.39 us                                                                                                               | 4.45 us: 1.01x slower                                                                                                     |
| pickle_dict          | 31.5 us                                                                                                               | 32.0 us: 1.02x slower                                                                                                     |
| xml_etree_parse      | 146 ms                                                                                                                | 149 ms: 1.02x slower                                                                                                      |
| unpickle_pure_python | 213 us                                                                                                                | 222 us: 1.04x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                                 | 1.01x faster                                                                                                              |

Benchmark hidden because not significant (2): json_loads, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                                                               | 13.8 ms: 1.05x slower                                                                                                     |
| python_startup_no_site | 8.83 ms                                                                                                               | 9.48 ms: 1.07x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                                 | 1.06x slower                                                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                                                                               | 9.14 ms: 1.13x faster                                                                                                     |
| django_template | 40.1 ms                                                                                                               | 41.4 ms: 1.03x slower                                                                                                     |
| genshi_text     | 26.7 ms                                                                                                               | 29.1 ms: 1.09x slower                                                                                                     |
| genshi_xml      | 58.6 ms                                                                                                               | 64.8 ms: 1.11x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                                 | 1.03x slower                                                                                                              |

All benchmarks:
===============

| Benchmark                | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|--------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads              | 2.48 sec                                                                                                              | 2.12 sec: 1.17x faster                                                                                                    |
| spectral_norm            | 97.9 ms                                                                                                               | 84.3 ms: 1.16x faster                                                                                                     |
| mako                     | 10.3 ms                                                                                                               | 9.14 ms: 1.13x faster                                                                                                     |
| richards                 | 51.9 ms                                                                                                               | 46.1 ms: 1.12x faster                                                                                                     |
| richards_super           | 58.9 ms                                                                                                               | 52.7 ms: 1.12x faster                                                                                                     |
| scimark_sparse_mat_mult  | 4.27 ms                                                                                                               | 3.91 ms: 1.09x faster                                                                                                     |
| nbody                    | 88.7 ms                                                                                                               | 81.6 ms: 1.09x faster                                                                                                     |
| float                    | 79.9 ms                                                                                                               | 74.2 ms: 1.08x faster                                                                                                     |
| fannkuch                 | 357 ms                                                                                                                | 336 ms: 1.06x faster                                                                                                      |
| scimark_fft              | 306 ms                                                                                                                | 288 ms: 1.06x faster                                                                                                      |
| xml_etree_generate       | 86.4 ms                                                                                                               | 81.8 ms: 1.06x faster                                                                                                     |
| xml_etree_process        | 60.8 ms                                                                                                               | 58.0 ms: 1.05x faster                                                                                                     |
| regex_compile            | 144 ms                                                                                                                | 138 ms: 1.05x faster                                                                                                      |
| crypto_pyaes             | 72.9 ms                                                                                                               | 70.2 ms: 1.04x faster                                                                                                     |
| pyflate                  | 478 ms                                                                                                                | 463 ms: 1.03x faster                                                                                                      |
| deepcopy_memo            | 39.1 us                                                                                                               | 37.8 us: 1.03x faster                                                                                                     |
| pprint_safe_repr         | 826 ms                                                                                                                | 802 ms: 1.03x faster                                                                                                      |
| async_tree_memoization   | 483 ms                                                                                                                | 470 ms: 1.03x faster                                                                                                      |
| xml_etree_iterparse      | 103 ms                                                                                                                | 101 ms: 1.02x faster                                                                                                      |
| telco                    | 8.33 ms                                                                                                               | 8.17 ms: 1.02x faster                                                                                                     |
| sqlite_synth             | 2.81 us                                                                                                               | 2.76 us: 1.02x faster                                                                                                     |
| logging_format           | 7.15 us                                                                                                               | 7.01 us: 1.02x faster                                                                                                     |
| json_dumps               | 10.8 ms                                                                                                               | 10.6 ms: 1.02x faster                                                                                                     |
| create_gc_cycles         | 2.01 ms                                                                                                               | 1.98 ms: 1.01x faster                                                                                                     |
| pprint_pformat           | 1.68 sec                                                                                                              | 1.66 sec: 1.01x faster                                                                                                    |
| dulwich_log              | 67.8 ms                                                                                                               | 67.0 ms: 1.01x faster                                                                                                     |
| async_tree_io_tg         | 917 ms                                                                                                                | 906 ms: 1.01x faster                                                                                                      |
| logging_simple           | 6.52 us                                                                                                               | 6.45 us: 1.01x faster                                                                                                     |
| pidigits                 | 253 ms                                                                                                                | 250 ms: 1.01x faster                                                                                                      |
| regex_dna                | 245 ms                                                                                                                | 243 ms: 1.01x faster                                                                                                      |
| unpickle                 | 15.5 us                                                                                                               | 15.4 us: 1.01x faster                                                                                                     |
| asyncio_tcp_ssl          | 1.58 sec                                                                                                              | 1.58 sec: 1.00x slower                                                                                                    |
| pickle_pure_python       | 316 us                                                                                                                | 318 us: 1.01x slower                                                                                                      |
| pathlib                  | 16.1 ms                                                                                                               | 16.2 ms: 1.01x slower                                                                                                     |
| asyncio_tcp              | 373 ms                                                                                                                | 377 ms: 1.01x slower                                                                                                      |
| unpickle_list            | 4.73 us                                                                                                               | 4.79 us: 1.01x slower                                                                                                     |
| html5lib                 | 73.3 ms                                                                                                               | 74.3 ms: 1.01x slower                                                                                                     |
| pickle_list              | 4.39 us                                                                                                               | 4.45 us: 1.01x slower                                                                                                     |
| generators               | 33.9 ms                                                                                                               | 34.4 ms: 1.01x slower                                                                                                     |
| sqlglot_parse            | 1.40 ms                                                                                                               | 1.42 ms: 1.01x slower                                                                                                     |
| pickle_dict              | 31.5 us                                                                                                               | 32.0 us: 1.02x slower                                                                                                     |
| thrift                   | 889 us                                                                                                                | 904 us: 1.02x slower                                                                                                      |
| pycparser                | 1.26 sec                                                                                                              | 1.28 sec: 1.02x slower                                                                                                    |
| meteor_contest           | 126 ms                                                                                                                | 129 ms: 1.02x slower                                                                                                      |
| json                     | 5.20 ms                                                                                                               | 5.30 ms: 1.02x slower                                                                                                     |
| chameleon                | 7.50 ms                                                                                                               | 7.68 ms: 1.02x slower                                                                                                     |
| dask                     | 397 ms                                                                                                                | 406 ms: 1.02x slower                                                                                                      |
| xml_etree_parse          | 146 ms                                                                                                                | 149 ms: 1.02x slower                                                                                                      |
| sqlglot_transpile        | 1.77 ms                                                                                                               | 1.82 ms: 1.03x slower                                                                                                     |
| go                       | 156 ms                                                                                                                | 161 ms: 1.03x slower                                                                                                      |
| regex_v8                 | 25.1 ms                                                                                                               | 26.0 ms: 1.03x slower                                                                                                     |
| django_template          | 40.1 ms                                                                                                               | 41.4 ms: 1.03x slower                                                                                                     |
| mdp                      | 2.49 sec                                                                                                              | 2.57 sec: 1.03x slower                                                                                                    |
| async_generators         | 367 ms                                                                                                                | 380 ms: 1.03x slower                                                                                                      |
| gc_traversal             | 4.71 ms                                                                                                               | 4.89 ms: 1.04x slower                                                                                                     |
| unpickle_pure_python     | 213 us                                                                                                                | 222 us: 1.04x slower                                                                                                      |
| chaos                    | 61.9 ms                                                                                                               | 64.4 ms: 1.04x slower                                                                                                     |
| tornado_http             | 119 ms                                                                                                                | 124 ms: 1.04x slower                                                                                                      |
| coverage                 | 81.2 ms                                                                                                               | 85.2 ms: 1.05x slower                                                                                                     |
| flaskblogging            | 4.73 ms                                                                                                               | 4.96 ms: 1.05x slower                                                                                                     |
| bench_thread_pool        | 915 us                                                                                                                | 961 us: 1.05x slower                                                                                                      |
| sympy_expand             | 507 ms                                                                                                                | 533 ms: 1.05x slower                                                                                                      |
| hexiom                   | 6.38 ms                                                                                                               | 6.70 ms: 1.05x slower                                                                                                     |
| docutils                 | 2.97 sec                                                                                                              | 3.13 sec: 1.05x slower                                                                                                    |
| comprehensions           | 17.0 us                                                                                                               | 17.9 us: 1.05x slower                                                                                                     |
| scimark_sor              | 124 ms                                                                                                                | 130 ms: 1.05x slower                                                                                                      |
| nqueens                  | 93.4 ms                                                                                                               | 98.4 ms: 1.05x slower                                                                                                     |
| python_startup           | 13.1 ms                                                                                                               | 13.8 ms: 1.05x slower                                                                                                     |
| 2to3                     | 288 ms                                                                                                                | 305 ms: 1.06x slower                                                                                                      |
| sqlglot_normalize        | 121 ms                                                                                                                | 128 ms: 1.06x slower                                                                                                      |
| sympy_str                | 296 ms                                                                                                                | 314 ms: 1.06x slower                                                                                                      |
| raytrace                 | 268 ms                                                                                                                | 284 ms: 1.06x slower                                                                                                      |
| sqlglot_optimize         | 59.5 ms                                                                                                               | 63.1 ms: 1.06x slower                                                                                                     |
| regex_effbot             | 3.46 ms                                                                                                               | 3.67 ms: 1.06x slower                                                                                                     |
| scimark_monte_carlo      | 63.6 ms                                                                                                               | 68.0 ms: 1.07x slower                                                                                                     |
| sympy_sum                | 155 ms                                                                                                                | 166 ms: 1.07x slower                                                                                                      |
| deepcopy_reduce          | 3.50 us                                                                                                               | 3.74 us: 1.07x slower                                                                                                     |
| typing_runtime_protocols | 173 us                                                                                                                | 185 us: 1.07x slower                                                                                                      |
| python_startup_no_site   | 8.83 ms                                                                                                               | 9.48 ms: 1.07x slower                                                                                                     |
| logging_silent           | 98.3 ns                                                                                                               | 107 ns: 1.09x slower                                                                                                      |
| genshi_text              | 26.7 ms                                                                                                               | 29.1 ms: 1.09x slower                                                                                                     |
| deepcopy                 | 388 us                                                                                                                | 427 us: 1.10x slower                                                                                                      |
| deltablue                | 3.38 ms                                                                                                               | 3.73 ms: 1.10x slower                                                                                                     |
| pylint                   | 345 ms                                                                                                                | 380 ms: 1.10x slower                                                                                                      |
| sympy_integrate          | 23.4 ms                                                                                                               | 25.8 ms: 1.10x slower                                                                                                     |
| genshi_xml               | 58.6 ms                                                                                                               | 64.8 ms: 1.11x slower                                                                                                     |
| scimark_lu               | 97.3 ms                                                                                                               | 119 ms: 1.22x slower                                                                                                      |
| Geometric mean           | (ref)                                                                                                                 | 1.01x slower                                                                                                              |

Benchmark hidden because not significant (11): coroutines, async_tree_none, bench_mp_pool, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, json_loads, asyncio_websockets, pickle

# HPT report

- Reliability score: 89.55% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x