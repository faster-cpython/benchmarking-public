# Results vs. 3.10.4

- fork: faster-cpython
- ref: refactor_refcnt_mort
- machine: linux-x86_64
- commit hash: 2fbc12f
- commit date: 2024-10-10
- overall geometric mean: 1.36x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 256 ms: 1.36x faster                                                            |
| docutils       | 3.30 sec                                               | 2.65 sec: 1.24x faster                                                          |
| html5lib       | 88.9 ms                                                | 62.6 ms: 1.42x faster                                                           |
| tornado_http   | 136 ms                                                 | 91.3 ms: 1.49x faster                                                           |
| Geometric mean | (ref)                                                  | 1.38x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 327 ms: 2.23x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 408 ms: 2.13x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 930 ms: 1.90x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 561 ms: 1.81x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 93.0 ms: 1.65x faster                                                           |
| float          | 117 ms                                                 | 79.1 ms: 1.48x faster                                                           |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                                            |
| regex_v8       | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                           |
| regex_dna      | 227 ms                                                 | 217 ms: 1.05x faster                                                            |
| regex_effbot   | 3.63 ms                                                | 3.57 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                  | 1.15x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 315 us: 1.54x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 224 us: 1.47x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 2.17 sec: 1.44x faster                                                          |
| xml_etree_process    | 79.1 ms                                                | 60.7 ms: 1.30x faster                                                           |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                           |
| json_loads           | 31.2 us                                                | 26.7 us: 1.17x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 87.8 ms: 1.13x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.09x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                                            |
| pickle_list          | 5.08 us                                                | 5.01 us: 1.01x faster                                                           |
| unpickle_list        | 5.20 us                                                | 5.38 us: 1.03x slower                                                           |
| unpickle             | 14.4 us                                                | 15.1 us: 1.05x slower                                                           |
| pickle               | 10.7 us                                                | 11.7 us: 1.09x slower                                                           |
| pickle_dict          | 29.6 us                                                | 34.0 us: 1.15x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.6 ms: 1.40x faster                                                           |
| django_template | 48.2 ms                                                | 35.0 ms: 1.38x faster                                                           |
| genshi_text     | 31.8 ms                                                | 23.5 ms: 1.35x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 51.8 ms: 1.28x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.33x faster                                                            |
| generators               | 80.1 ms                                                | 28.2 ms: 2.84x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.36 ms: 2.36x faster                                                           |
| async_tree_none          | 728 ms                                                 | 327 ms: 2.23x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 408 ms: 2.13x faster                                                            |
| go                       | 240 ms                                                 | 123 ms: 1.96x faster                                                            |
| asyncio_tcp              | 922 ms                                                 | 479 ms: 1.92x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 930 ms: 1.90x faster                                                            |
| chaos                    | 115 ms                                                 | 61.2 ms: 1.89x faster                                                           |
| raytrace                 | 507 ms                                                 | 275 ms: 1.85x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 32.2 us: 1.82x faster                                                           |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 561 ms: 1.81x faster                                                            |
| logging_silent           | 190 ns                                                 | 106 ns: 1.80x faster                                                            |
| deepcopy                 | 479 us                                                 | 268 us: 1.79x faster                                                            |
| richards_super           | 94.7 ms                                                | 53.3 ms: 1.78x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 72.1 ms: 1.77x faster                                                           |
| pylint                   | 551 ms                                                 | 320 ms: 1.72x faster                                                            |
| scimark_monte_carlo      | 118 ms                                                 | 69.2 ms: 1.71x faster                                                           |
| scimark_sor              | 220 ms                                                 | 129 ms: 1.71x faster                                                            |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                                           |
| richards                 | 79.3 ms                                                | 47.1 ms: 1.68x faster                                                           |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.65x faster                                                           |
| nbody                    | 154 ms                                                 | 93.0 ms: 1.65x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.39 ms: 1.63x faster                                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.61 ms: 1.59x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 315 us: 1.54x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.76 us: 1.51x faster                                                           |
| tornado_http             | 136 ms                                                 | 91.3 ms: 1.49x faster                                                           |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                                            |
| pyflate                  | 716 ms                                                 | 483 ms: 1.48x faster                                                            |
| float                    | 117 ms                                                 | 79.1 ms: 1.48x faster                                                           |
| unpickle_pure_python     | 331 us                                                 | 224 us: 1.47x faster                                                            |
| logging_simple           | 8.30 us                                                | 5.69 us: 1.46x faster                                                           |
| coroutines               | 35.1 ms                                                | 24.2 ms: 1.45x faster                                                           |
| spectral_norm            | 170 ms                                                 | 117 ms: 1.45x faster                                                            |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 2.17 sec: 1.44x faster                                                          |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                                          |
| logging_format           | 9.09 us                                                | 6.35 us: 1.43x faster                                                           |
| html5lib                 | 88.9 ms                                                | 62.6 ms: 1.42x faster                                                           |
| mako                     | 16.3 ms                                                | 11.6 ms: 1.40x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.39x faster                                                          |
| pprint_safe_repr         | 1.02 sec                                               | 736 ms: 1.38x faster                                                            |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                           |
| django_template          | 48.2 ms                                                | 35.0 ms: 1.38x faster                                                           |
| thrift                   | 1.07 ms                                                | 783 us: 1.37x faster                                                            |
| 2to3                     | 348 ms                                                 | 256 ms: 1.36x faster                                                            |
| genshi_text              | 31.8 ms                                                | 23.5 ms: 1.35x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.33x faster                                                          |
| nqueens                  | 106 ms                                                 | 80.3 ms: 1.32x faster                                                           |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.93 ms: 1.31x faster                                                           |
| xml_etree_process        | 79.1 ms                                                | 60.7 ms: 1.30x faster                                                           |
| sqlglot_normalize        | 143 ms                                                 | 110 ms: 1.30x faster                                                            |
| dulwich_log              | 84.3 ms                                                | 65.4 ms: 1.29x faster                                                           |
| fannkuch                 | 532 ms                                                 | 413 ms: 1.29x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 20.1 ms: 1.28x faster                                                           |
| genshi_xml               | 66.0 ms                                                | 51.8 ms: 1.28x faster                                                           |
| sympy_str                | 346 ms                                                 | 272 ms: 1.27x faster                                                            |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                           |
| sqlglot_optimize         | 69.2 ms                                                | 54.5 ms: 1.27x faster                                                           |
| scimark_fft              | 466 ms                                                 | 373 ms: 1.25x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.65 sec: 1.24x faster                                                          |
| sympy_expand             | 566 ms                                                 | 463 ms: 1.22x faster                                                            |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                           |
| unpack_sequence          | 60.0 ns                                                | 49.7 ns: 1.21x faster                                                           |
| json                     | 5.69 ms                                                | 4.85 ms: 1.17x faster                                                           |
| json_loads               | 31.2 us                                                | 26.7 us: 1.17x faster                                                           |
| bench_thread_pool        | 986 us                                                 | 850 us: 1.16x faster                                                            |
| regex_v8                 | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                           |
| xml_etree_generate       | 99.4 ms                                                | 87.8 ms: 1.13x faster                                                           |
| mdp                      | 2.85 sec                                               | 2.52 sec: 1.13x faster                                                          |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.09x faster                                                            |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.86 us: 1.06x faster                                                           |
| regex_dna                | 227 ms                                                 | 217 ms: 1.05x faster                                                            |
| regex_effbot             | 3.63 ms                                                | 3.57 ms: 1.02x faster                                                           |
| pickle_list              | 5.08 us                                                | 5.01 us: 1.01x faster                                                           |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                            |
| async_generators         | 444 ms                                                 | 438 ms: 1.01x faster                                                            |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                            |
| unpickle_list            | 5.20 us                                                | 5.38 us: 1.03x slower                                                           |
| unpickle                 | 14.4 us                                                | 15.1 us: 1.05x slower                                                           |
| pickle                   | 10.7 us                                                | 11.7 us: 1.09x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.78 ms: 1.10x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 3.98 ms: 1.10x slower                                                           |
| telco                    | 7.27 ms                                                | 8.02 ms: 1.10x slower                                                           |
| pickle_dict              | 29.6 us                                                | 34.0 us: 1.15x slower                                                           |
| coverage                 | 79.4 ms                                                | 91.8 ms: 1.16x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                           |
| bench_mp_pool            | 24.0 ms                                                | 56.3 ms: 2.35x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.36x faster                                                                    |
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241010-3.14.0a0-2fbc12f/bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.11x