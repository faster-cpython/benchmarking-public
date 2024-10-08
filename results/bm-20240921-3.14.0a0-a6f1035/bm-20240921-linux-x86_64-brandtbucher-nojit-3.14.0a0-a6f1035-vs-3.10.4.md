# Results vs. 3.10.4

- fork: brandtbucher
- ref: nojit
- machine: linux-x86_64
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.39x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 255 ms: 1.37x faster                                         |
| docutils       | 3.30 sec                                               | 2.65 sec: 1.24x faster                                       |
| html5lib       | 88.9 ms                                                | 63.8 ms: 1.39x faster                                        |
| tornado_http   | 136 ms                                                 | 89.8 ms: 1.52x faster                                        |
| Geometric mean | (ref)                                                  | 1.38x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 312 ms: 2.33x faster                                         |
| async_tree_memoization  | 870 ms                                                 | 389 ms: 2.23x faster                                         |
| async_tree_io           | 1.77 sec                                               | 879 ms: 2.01x faster                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 561 ms: 1.81x faster                                         |
| Geometric mean          | (ref)                                                  | 2.09x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 87.1 ms: 1.76x faster                                        |
| float          | 117 ms                                                 | 76.3 ms: 1.53x faster                                        |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                         |
| Geometric mean | (ref)                                                  | 1.40x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                         |
| regex_v8       | 27.8 ms                                                | 25.0 ms: 1.11x faster                                        |
| regex_dna      | 227 ms                                                 | 221 ms: 1.03x faster                                         |
| regex_effbot   | 3.63 ms                                                | 3.70 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                  | 1.13x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 301 us: 1.61x faster                                         |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                         |
| tomli_loads          | 3.14 sec                                               | 2.11 sec: 1.49x faster                                       |
| json_dumps           | 14.2 ms                                                | 10.6 ms: 1.34x faster                                        |
| xml_etree_process    | 79.1 ms                                                | 59.0 ms: 1.34x faster                                        |
| xml_etree_generate   | 99.4 ms                                                | 84.7 ms: 1.17x faster                                        |
| json_loads           | 31.2 us                                                | 27.5 us: 1.14x faster                                        |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                         |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                         |
| pickle_list          | 5.08 us                                                | 5.12 us: 1.01x slower                                        |
| unpickle_list        | 5.20 us                                                | 5.34 us: 1.03x slower                                        |
| unpickle             | 14.4 us                                                | 15.2 us: 1.06x slower                                        |
| pickle               | 10.7 us                                                | 11.6 us: 1.09x slower                                        |
| pickle_dict          | 29.6 us                                                | 35.1 us: 1.19x slower                                        |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                        |
| python_startup_no_site | 5.93 ms                                                | 7.00 ms: 1.18x slower                                        |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.3 ms: 1.44x faster                                        |
| genshi_text     | 31.8 ms                                                | 22.4 ms: 1.42x faster                                        |
| django_template | 48.2 ms                                                | 34.1 ms: 1.41x faster                                        |
| genshi_xml      | 66.0 ms                                                | 50.0 ms: 1.32x faster                                        |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 160 us: 3.41x faster                                         |
| generators               | 80.1 ms                                                | 27.7 ms: 2.89x faster                                        |
| deltablue                | 7.91 ms                                                | 3.23 ms: 2.45x faster                                        |
| async_tree_none          | 728 ms                                                 | 312 ms: 2.33x faster                                         |
| async_tree_memoization   | 870 ms                                                 | 389 ms: 2.23x faster                                         |
| async_tree_io            | 1.77 sec                                               | 879 ms: 2.01x faster                                         |
| go                       | 240 ms                                                 | 120 ms: 2.00x faster                                         |
| asyncio_tcp              | 922 ms                                                 | 468 ms: 1.97x faster                                         |
| deepcopy_memo            | 58.5 us                                                | 29.7 us: 1.97x faster                                        |
| chaos                    | 115 ms                                                 | 58.8 ms: 1.96x faster                                        |
| raytrace                 | 507 ms                                                 | 264 ms: 1.92x faster                                         |
| logging_silent           | 190 ns                                                 | 102 ns: 1.86x faster                                         |
| deepcopy                 | 479 us                                                 | 258 us: 1.86x faster                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 561 ms: 1.81x faster                                         |
| richards_super           | 94.7 ms                                                | 52.7 ms: 1.80x faster                                        |
| nbody                    | 154 ms                                                 | 87.1 ms: 1.76x faster                                        |
| scimark_sor              | 220 ms                                                 | 125 ms: 1.76x faster                                         |
| scimark_monte_carlo      | 118 ms                                                 | 67.4 ms: 1.75x faster                                        |
| crypto_pyaes             | 128 ms                                                 | 73.2 ms: 1.75x faster                                        |
| pylint                   | 551 ms                                                 | 319 ms: 1.73x faster                                         |
| richards                 | 79.3 ms                                                | 46.4 ms: 1.71x faster                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                        |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                        |
| hexiom                   | 10.4 ms                                                | 6.26 ms: 1.66x faster                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                        |
| pickle_pure_python       | 484 us                                                 | 301 us: 1.61x faster                                         |
| scimark_lu               | 176 ms                                                 | 112 ms: 1.58x faster                                         |
| pyflate                  | 716 ms                                                 | 460 ms: 1.56x faster                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                        |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                         |
| float                    | 117 ms                                                 | 76.3 ms: 1.53x faster                                        |
| tornado_http             | 136 ms                                                 | 89.8 ms: 1.52x faster                                        |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.51x faster                                        |
| tomli_loads              | 3.14 sec                                               | 2.11 sec: 1.49x faster                                       |
| logging_format           | 9.09 us                                                | 6.17 us: 1.47x faster                                        |
| logging_simple           | 8.30 us                                                | 5.65 us: 1.47x faster                                        |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                         |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.78 sec: 1.45x faster                                       |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                       |
| spectral_norm            | 170 ms                                                 | 118 ms: 1.44x faster                                         |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.44x faster                                        |
| pprint_safe_repr         | 1.02 sec                                               | 711 ms: 1.43x faster                                         |
| genshi_text              | 31.8 ms                                                | 22.4 ms: 1.42x faster                                        |
| django_template          | 48.2 ms                                                | 34.1 ms: 1.41x faster                                        |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                       |
| html5lib                 | 88.9 ms                                                | 63.8 ms: 1.39x faster                                        |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                        |
| thrift                   | 1.07 ms                                                | 780 us: 1.37x faster                                         |
| 2to3                     | 348 ms                                                 | 255 ms: 1.37x faster                                         |
| json_dumps               | 14.2 ms                                                | 10.6 ms: 1.34x faster                                        |
| xml_etree_process        | 79.1 ms                                                | 59.0 ms: 1.34x faster                                        |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                         |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.33x faster                                         |
| genshi_xml               | 66.0 ms                                                | 50.0 ms: 1.32x faster                                        |
| sympy_integrate          | 25.8 ms                                                | 19.7 ms: 1.31x faster                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.96 ms: 1.30x faster                                        |
| dulwich_log              | 84.3 ms                                                | 64.7 ms: 1.30x faster                                        |
| nqueens                  | 106 ms                                                 | 81.4 ms: 1.30x faster                                        |
| fannkuch                 | 532 ms                                                 | 410 ms: 1.30x faster                                         |
| sqlglot_optimize         | 69.2 ms                                                | 53.5 ms: 1.29x faster                                        |
| sympy_str                | 346 ms                                                 | 269 ms: 1.29x faster                                         |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                        |
| scimark_fft              | 466 ms                                                 | 368 ms: 1.27x faster                                         |
| docutils                 | 3.30 sec                                               | 2.65 sec: 1.24x faster                                       |
| sympy_expand             | 566 ms                                                 | 456 ms: 1.24x faster                                         |
| bench_thread_pool        | 986 us                                                 | 809 us: 1.22x faster                                         |
| unpack_sequence          | 60.0 ns                                                | 50.3 ns: 1.19x faster                                        |
| xml_etree_generate       | 99.4 ms                                                | 84.7 ms: 1.17x faster                                        |
| json_loads               | 31.2 us                                                | 27.5 us: 1.14x faster                                        |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                         |
| json                     | 5.69 ms                                                | 5.09 ms: 1.12x faster                                        |
| regex_v8                 | 27.8 ms                                                | 25.0 ms: 1.11x faster                                        |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                         |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                         |
| sqlite_synth             | 3.02 us                                                | 2.85 us: 1.06x faster                                        |
| mdp                      | 2.85 sec                                               | 2.73 sec: 1.04x faster                                       |
| regex_dna                | 227 ms                                                 | 221 ms: 1.03x faster                                         |
| async_generators         | 444 ms                                                 | 434 ms: 1.02x faster                                         |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                         |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                         |
| pickle_list              | 5.08 us                                                | 5.12 us: 1.01x slower                                        |
| regex_effbot             | 3.63 ms                                                | 3.70 ms: 1.02x slower                                        |
| unpickle_list            | 5.20 us                                                | 5.34 us: 1.03x slower                                        |
| unpickle                 | 14.4 us                                                | 15.2 us: 1.06x slower                                        |
| gc_traversal             | 3.62 ms                                                | 3.88 ms: 1.07x slower                                        |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.07x slower                                        |
| coverage                 | 79.4 ms                                                | 85.2 ms: 1.07x slower                                        |
| pickle                   | 10.7 us                                                | 11.6 us: 1.09x slower                                        |
| telco                    | 7.27 ms                                                | 8.40 ms: 1.16x slower                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.00 ms: 1.18x slower                                        |
| pickle_dict              | 29.6 us                                                | 35.1 us: 1.19x slower                                        |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                 |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240921-3.14.0a0-a6f1035/bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.12x