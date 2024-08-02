# Results vs. 3.10.4

- fork: python
- ref: df13a1821a90fcfb75ec
- machine: linux-x86_64
- commit hash: df13a18
- commit date: 2024-08-01
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 274 ms: 1.27x faster                                                  |
| docutils       | 3.30 sec                                               | 2.91 sec: 1.13x faster                                                |
| html5lib       | 88.9 ms                                                | 65.2 ms: 1.36x faster                                                 |
| tornado_http   | 136 ms                                                 | 92.3 ms: 1.48x faster                                                 |
| Geometric mean | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 328 ms: 2.22x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 426 ms: 2.04x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 910 ms: 1.94x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 568 ms: 1.79x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.99x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.8 ms: 1.92x faster                                                 |
| float          | 117 ms                                                 | 71.6 ms: 1.64x faster                                                 |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.48x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 133 ms: 1.42x faster                                                  |
| regex_v8       | 27.8 ms                                                | 25.2 ms: 1.10x faster                                                 |
| regex_dna      | 227 ms                                                 | 223 ms: 1.02x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.75 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 297 us: 1.63x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 56.0 ms: 1.41x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 80.0 ms: 1.24x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 99.8 ms: 1.16x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.14x faster                                                  |
| json_loads           | 31.2 us                                                | 27.9 us: 1.12x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.14 ms: 1.20x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.82 ms: 1.66x faster                                                 |
| django_template | 48.2 ms                                                | 36.0 ms: 1.34x faster                                                 |
| genshi_text     | 31.8 ms                                                | 24.7 ms: 1.29x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 54.5 ms: 1.21x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.36x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.23x faster                                                  |
| generators               | 80.1 ms                                                | 33.1 ms: 2.42x faster                                                 |
| async_tree_none          | 728 ms                                                 | 328 ms: 2.22x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.60 ms: 2.20x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 426 ms: 2.04x faster                                                  |
| richards_super           | 94.7 ms                                                | 46.8 ms: 2.03x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 29.0 us: 2.01x faster                                                 |
| chaos                    | 115 ms                                                 | 57.8 ms: 2.00x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 910 ms: 1.94x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 60.9 ms: 1.94x faster                                                 |
| richards                 | 79.3 ms                                                | 41.1 ms: 1.93x faster                                                 |
| nbody                    | 154 ms                                                 | 79.8 ms: 1.92x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 67.4 ms: 1.90x faster                                                 |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 490 ms: 1.88x faster                                                  |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                                  |
| logging_silent           | 190 ns                                                 | 106 ns: 1.80x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 568 ms: 1.79x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.2 us: 1.77x faster                                                 |
| deepcopy                 | 479 us                                                 | 273 us: 1.76x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.67x faster                                                 |
| mako                     | 16.3 ms                                                | 9.82 ms: 1.66x faster                                                 |
| pyflate                  | 716 ms                                                 | 433 ms: 1.65x faster                                                  |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.65x faster                                                  |
| go                       | 240 ms                                                 | 146 ms: 1.64x faster                                                  |
| float                    | 117 ms                                                 | 71.6 ms: 1.64x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 297 us: 1.63x faster                                                  |
| scimark_lu               | 176 ms                                                 | 109 ms: 1.62x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                                 |
| pylint                   | 551 ms                                                 | 355 ms: 1.55x faster                                                  |
| coroutines               | 35.1 ms                                                | 22.6 ms: 1.55x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.73 ms: 1.55x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.24 ms: 1.53x faster                                                 |
| logging_format           | 9.09 us                                                | 6.06 us: 1.50x faster                                                 |
| scimark_fft              | 466 ms                                                 | 311 ms: 1.50x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.57 us: 1.49x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.82 us: 1.48x faster                                                 |
| tornado_http             | 136 ms                                                 | 92.3 ms: 1.48x faster                                                 |
| fannkuch                 | 532 ms                                                 | 369 ms: 1.44x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                |
| regex_compile            | 188 ms                                                 | 133 ms: 1.42x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 56.0 ms: 1.41x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                                |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 738 ms: 1.38x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                 |
| html5lib                 | 88.9 ms                                                | 65.2 ms: 1.36x faster                                                 |
| thrift                   | 1.07 ms                                                | 794 us: 1.35x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.34x faster                                                |
| django_template          | 48.2 ms                                                | 36.0 ms: 1.34x faster                                                 |
| genshi_text              | 31.8 ms                                                | 24.7 ms: 1.29x faster                                                 |
| 2to3                     | 348 ms                                                 | 274 ms: 1.27x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.27x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.26x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 80.0 ms: 1.24x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 55.8 ms: 1.24x faster                                                 |
| nqueens                  | 106 ms                                                 | 86.4 ms: 1.22x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 54.5 ms: 1.21x faster                                                 |
| dask                     | 441 ms                                                 | 365 ms: 1.21x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 821 us: 1.20x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 99.8 ms: 1.16x faster                                                 |
| sympy_sum                | 196 ms                                                 | 170 ms: 1.16x faster                                                  |
| sympy_str                | 346 ms                                                 | 300 ms: 1.15x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.14x faster                                                  |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 22.6 ms: 1.14x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.91 sec: 1.13x faster                                                |
| json_loads               | 31.2 us                                                | 27.9 us: 1.12x faster                                                 |
| json                     | 5.69 ms                                                | 5.13 ms: 1.11x faster                                                 |
| sympy_expand             | 566 ms                                                 | 510 ms: 1.11x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 25.2 ms: 1.10x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.63 sec: 1.08x faster                                                |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                  |
| regex_dna                | 227 ms                                                 | 223 ms: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                  |
| gc_traversal             | 3.62 ms                                                | 3.74 ms: 1.03x slower                                                 |
| regex_effbot             | 3.63 ms                                                | 3.75 ms: 1.03x slower                                                 |
| async_generators         | 444 ms                                                 | 466 ms: 1.05x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.09x slower                                                 |
| telco                    | 7.27 ms                                                | 7.95 ms: 1.09x slower                                                 |
| coverage                 | 79.4 ms                                                | 91.3 ms: 1.15x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.14 ms: 1.20x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240801-3.14.0a0-df13a18-JIT/bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.19x