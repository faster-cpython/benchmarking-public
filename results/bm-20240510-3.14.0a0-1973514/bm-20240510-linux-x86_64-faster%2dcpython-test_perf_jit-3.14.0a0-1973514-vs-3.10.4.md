# Results vs. 3.10.4

- fork: faster-cpython
- ref: test_perf_jit
- machine: linux-x86_64
- commit hash: 1973514
- commit date: 2024-05-10
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 270 ms: 1.29x faster                                                     |
| chameleon      | 9.68 ms                                                | 6.94 ms: 1.40x faster                                                    |
| docutils       | 3.30 sec                                               | 2.81 sec: 1.17x faster                                                   |
| html5lib       | 88.9 ms                                                | 66.6 ms: 1.33x faster                                                    |
| tornado_http   | 136 ms                                                 | 94.5 ms: 1.44x faster                                                    |
| Geometric mean | (ref)                                                  | 1.32x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 362 ms: 2.01x faster                                                     |
| async_tree_io           | 1.77 sec                                               | 935 ms: 1.89x faster                                                     |
| async_tree_memoization  | 870 ms                                                 | 479 ms: 1.82x faster                                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 617 ms: 1.65x faster                                                     |
| Geometric mean          | (ref)                                                  | 1.84x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 90.1 ms: 1.70x faster                                                    |
| float          | 117 ms                                                 | 77.2 ms: 1.52x faster                                                    |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.38x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 136 ms: 1.39x faster                                                     |
| regex_v8       | 27.8 ms                                                | 25.9 ms: 1.07x faster                                                    |
| regex_dna      | 227 ms                                                 | 220 ms: 1.03x faster                                                     |
| regex_effbot   | 3.63 ms                                                | 3.73 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                  | 1.11x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 306 us: 1.58x faster                                                     |
| tomli_loads          | 3.14 sec                                               | 2.08 sec: 1.51x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 221 us: 1.50x faster                                                     |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                    |
| xml_etree_process    | 79.1 ms                                                | 61.8 ms: 1.28x faster                                                    |
| xml_etree_generate   | 99.4 ms                                                | 89.5 ms: 1.11x faster                                                    |
| json_loads           | 31.2 us                                                | 28.8 us: 1.08x faster                                                    |
| xml_etree_iterparse  | 115 ms                                                 | 107 ms: 1.08x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 162 ms: 1.04x faster                                                     |
| unpickle_list        | 5.20 us                                                | 5.48 us: 1.05x slower                                                    |
| pickle               | 10.7 us                                                | 11.6 us: 1.09x slower                                                    |
| pickle_list          | 5.08 us                                                | 5.63 us: 1.11x slower                                                    |
| unpickle             | 14.4 us                                                | 16.2 us: 1.13x slower                                                    |
| pickle_dict          | 29.6 us                                                | 34.0 us: 1.15x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.4 ms: 1.40x faster                                                    |
| python_startup_no_site | 5.93 ms                                                | 7.12 ms: 1.20x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                    |
| genshi_text     | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                    |
| django_template | 48.2 ms                                                | 35.1 ms: 1.37x faster                                                    |
| genshi_xml      | 66.0 ms                                                | 50.6 ms: 1.31x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                                     |
| generators               | 80.1 ms                                                | 29.6 ms: 2.70x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.27 ms: 2.42x faster                                                    |
| async_tree_none          | 728 ms                                                 | 362 ms: 2.01x faster                                                     |
| chaos                    | 115 ms                                                 | 60.4 ms: 1.91x faster                                                    |
| async_tree_io            | 1.77 sec                                               | 935 ms: 1.89x faster                                                     |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                                     |
| logging_silent           | 190 ns                                                 | 103 ns: 1.84x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 506 ms: 1.82x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 479 ms: 1.82x faster                                                     |
| richards_super           | 94.7 ms                                                | 54.2 ms: 1.75x faster                                                    |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.74x faster                                                     |
| pylint                   | 551 ms                                                 | 317 ms: 1.74x faster                                                     |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                    |
| scimark_monte_carlo      | 118 ms                                                 | 68.5 ms: 1.73x faster                                                    |
| nbody                    | 154 ms                                                 | 90.1 ms: 1.70x faster                                                    |
| crypto_pyaes             | 128 ms                                                 | 75.2 ms: 1.70x faster                                                    |
| go                       | 240 ms                                                 | 143 ms: 1.68x faster                                                     |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.66x faster                                                    |
| richards                 | 79.3 ms                                                | 47.8 ms: 1.66x faster                                                    |
| hexiom                   | 10.4 ms                                                | 6.29 ms: 1.65x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 617 ms: 1.65x faster                                                     |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                                    |
| pickle_pure_python       | 484 us                                                 | 306 us: 1.58x faster                                                     |
| float                    | 117 ms                                                 | 77.2 ms: 1.52x faster                                                    |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                    |
| tomli_loads              | 3.14 sec                                               | 2.08 sec: 1.51x faster                                                   |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                                     |
| spectral_norm            | 170 ms                                                 | 114 ms: 1.50x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 221 us: 1.50x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 39.3 us: 1.49x faster                                                    |
| pyflate                  | 716 ms                                                 | 484 ms: 1.48x faster                                                     |
| logging_simple           | 8.30 us                                                | 5.64 us: 1.47x faster                                                    |
| logging_format           | 9.09 us                                                | 6.30 us: 1.44x faster                                                    |
| tornado_http             | 136 ms                                                 | 94.5 ms: 1.44x faster                                                    |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                    |
| python_startup           | 14.6 ms                                                | 10.4 ms: 1.40x faster                                                    |
| chameleon                | 9.68 ms                                                | 6.94 ms: 1.40x faster                                                    |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.84 sec: 1.39x faster                                                   |
| regex_compile            | 188 ms                                                 | 136 ms: 1.39x faster                                                     |
| genshi_text              | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                    |
| django_template          | 48.2 ms                                                | 35.1 ms: 1.37x faster                                                    |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.57 sec: 1.34x faster                                                   |
| html5lib                 | 88.9 ms                                                | 66.6 ms: 1.33x faster                                                    |
| thrift                   | 1.07 ms                                                | 805 us: 1.33x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 771 ms: 1.32x faster                                                     |
| deepcopy                 | 479 us                                                 | 364 us: 1.32x faster                                                     |
| fannkuch                 | 532 ms                                                 | 407 ms: 1.31x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 50.6 ms: 1.31x faster                                                    |
| deepcopy_reduce          | 4.17 us                                                | 3.22 us: 1.30x faster                                                    |
| sqlglot_normalize        | 143 ms                                                 | 110 ms: 1.29x faster                                                     |
| nqueens                  | 106 ms                                                 | 81.9 ms: 1.29x faster                                                    |
| 2to3                     | 348 ms                                                 | 270 ms: 1.29x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 61.8 ms: 1.28x faster                                                    |
| dulwich_log              | 84.3 ms                                                | 65.9 ms: 1.28x faster                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.12 ms: 1.26x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 20.4 ms: 1.26x faster                                                    |
| sympy_sum                | 196 ms                                                 | 156 ms: 1.26x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 55.2 ms: 1.25x faster                                                    |
| scimark_fft              | 466 ms                                                 | 377 ms: 1.24x faster                                                     |
| sympy_str                | 346 ms                                                 | 282 ms: 1.22x faster                                                     |
| dask                     | 441 ms                                                 | 368 ms: 1.20x faster                                                     |
| sympy_expand             | 566 ms                                                 | 474 ms: 1.19x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 831 us: 1.19x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.81 sec: 1.17x faster                                                   |
| pathlib                  | 20.5 ms                                                | 17.6 ms: 1.16x faster                                                    |
| xml_etree_generate       | 99.4 ms                                                | 89.5 ms: 1.11x faster                                                    |
| mdp                      | 2.85 sec                                               | 2.58 sec: 1.10x faster                                                   |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.09x faster                                                     |
| json_loads               | 31.2 us                                                | 28.8 us: 1.08x faster                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 107 ms: 1.08x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 25.9 ms: 1.07x faster                                                    |
| xml_etree_parse          | 168 ms                                                 | 162 ms: 1.04x faster                                                     |
| regex_dna                | 227 ms                                                 | 220 ms: 1.03x faster                                                     |
| json                     | 5.69 ms                                                | 5.53 ms: 1.03x faster                                                    |
| sqlite_synth             | 3.02 us                                                | 2.95 us: 1.02x faster                                                    |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                     |
| bench_mp_pool            | 24.0 ms                                                | 23.8 ms: 1.01x faster                                                    |
| asyncio_websockets       | 559 ms                                                 | 564 ms: 1.01x slower                                                     |
| async_generators         | 444 ms                                                 | 452 ms: 1.02x slower                                                     |
| regex_effbot             | 3.63 ms                                                | 3.73 ms: 1.03x slower                                                    |
| flaskblogging            | 8.58 ms                                                | 8.88 ms: 1.03x slower                                                    |
| unpickle_list            | 5.20 us                                                | 5.48 us: 1.05x slower                                                    |
| gc_traversal             | 3.62 ms                                                | 3.82 ms: 1.06x slower                                                    |
| pickle                   | 10.7 us                                                | 11.6 us: 1.09x slower                                                    |
| pickle_list              | 5.08 us                                                | 5.63 us: 1.11x slower                                                    |
| create_gc_cycles         | 1.62 ms                                                | 1.80 ms: 1.11x slower                                                    |
| unpickle                 | 14.4 us                                                | 16.2 us: 1.13x slower                                                    |
| pickle_dict              | 29.6 us                                                | 34.0 us: 1.15x slower                                                    |
| coverage                 | 79.4 ms                                                | 92.7 ms: 1.17x slower                                                    |
| python_startup_no_site   | 5.93 ms                                                | 7.12 ms: 1.20x slower                                                    |
| telco                    | 7.27 ms                                                | 177 ms: 24.32x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                             |
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, djangocms, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240510-3.14.0a0-1973514/bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.10x