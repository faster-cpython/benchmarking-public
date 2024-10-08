# Results vs. 3.10.4

- fork: brandtbucher
- ref: underflow_known_dyna
- machine: linux-x86_64
- commit hash: 7ad3776
- commit date: 2024-09-06
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 285 ms: 1.22x faster                                                        |
| docutils       | 3.30 sec                                               | 3.25 sec: 1.01x faster                                                      |
| html5lib       | 88.9 ms                                                | 69.1 ms: 1.29x faster                                                       |
| tornado_http   | 136 ms                                                 | 103 ms: 1.32x faster                                                        |
| Geometric mean | (ref)                                                  | 1.20x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.23x faster                                                        |
| async_tree_memoization  | 870 ms                                                 | 406 ms: 2.14x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 933 ms: 1.89x faster                                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 563 ms: 1.81x faster                                                        |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.6 ms: 1.93x faster                                                       |
| float          | 117 ms                                                 | 70.9 ms: 1.65x faster                                                       |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.49x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 151 ms: 1.25x faster                                                        |
| regex_v8       | 27.8 ms                                                | 24.6 ms: 1.13x faster                                                       |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 201 us: 1.64x faster                                                        |
| tomli_loads          | 3.14 sec                                               | 2.00 sec: 1.57x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 310 us: 1.56x faster                                                        |
| xml_etree_process    | 79.1 ms                                                | 54.3 ms: 1.46x faster                                                       |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 77.8 ms: 1.28x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 98.7 ms: 1.17x faster                                                       |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                                        |
| json_loads           | 31.2 us                                                | 28.5 us: 1.09x faster                                                       |
| unpickle_list        | 5.20 us                                                | 5.29 us: 1.02x slower                                                       |
| pickle_list          | 5.08 us                                                | 5.27 us: 1.04x slower                                                       |
| unpickle             | 14.4 us                                                | 15.1 us: 1.05x slower                                                       |
| pickle               | 10.7 us                                                | 11.6 us: 1.09x slower                                                       |
| pickle_dict          | 29.6 us                                                | 34.1 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                       |
| python_startup_no_site | 5.93 ms                                                | 7.17 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.70 ms: 1.68x faster                                                       |
| genshi_text     | 31.8 ms                                                | 23.9 ms: 1.33x faster                                                       |
| django_template | 48.2 ms                                                | 37.9 ms: 1.27x faster                                                       |
| genshi_xml      | 66.0 ms                                                | 63.5 ms: 1.04x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.31x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.33x faster                                                        |
| deltablue                | 7.91 ms                                                | 3.24 ms: 2.44x faster                                                       |
| generators               | 80.1 ms                                                | 33.2 ms: 2.41x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 26.0 us: 2.25x faster                                                       |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.23x faster                                                        |
| richards_super           | 94.7 ms                                                | 42.8 ms: 2.21x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 406 ms: 2.14x faster                                                        |
| richards                 | 79.3 ms                                                | 38.4 ms: 2.06x faster                                                       |
| chaos                    | 115 ms                                                 | 58.5 ms: 1.97x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 65.4 ms: 1.95x faster                                                       |
| logging_silent           | 190 ns                                                 | 97.3 ns: 1.95x faster                                                       |
| nbody                    | 154 ms                                                 | 79.6 ms: 1.93x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 933 ms: 1.89x faster                                                        |
| asyncio_tcp              | 922 ms                                                 | 500 ms: 1.84x faster                                                        |
| raytrace                 | 507 ms                                                 | 275 ms: 1.84x faster                                                        |
| deepcopy                 | 479 us                                                 | 263 us: 1.83x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 563 ms: 1.81x faster                                                        |
| scimark_sor              | 220 ms                                                 | 124 ms: 1.77x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 67.4 ms: 1.75x faster                                                       |
| go                       | 240 ms                                                 | 138 ms: 1.75x faster                                                        |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                       |
| spectral_norm            | 170 ms                                                 | 99.9 ms: 1.70x faster                                                       |
| mako                     | 16.3 ms                                                | 9.70 ms: 1.68x faster                                                       |
| float                    | 117 ms                                                 | 70.9 ms: 1.65x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 201 us: 1.64x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.64 us: 1.58x faster                                                       |
| tomli_loads              | 3.14 sec                                               | 2.00 sec: 1.57x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 310 us: 1.56x faster                                                        |
| pyflate                  | 716 ms                                                 | 462 ms: 1.55x faster                                                        |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.54x faster                                                        |
| hexiom                   | 10.4 ms                                                | 6.86 ms: 1.51x faster                                                       |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                       |
| scimark_fft              | 466 ms                                                 | 309 ms: 1.51x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 54.3 ms: 1.46x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.44 ms: 1.46x faster                                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.78 ms: 1.45x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.52 ms: 1.43x faster                                                       |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.42x faster                                                      |
| logging_format           | 9.09 us                                                | 6.42 us: 1.42x faster                                                       |
| logging_simple           | 8.30 us                                                | 5.91 us: 1.41x faster                                                       |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                                      |
| fannkuch                 | 532 ms                                                 | 382 ms: 1.39x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 738 ms: 1.38x faster                                                        |
| thrift                   | 1.07 ms                                                | 780 us: 1.37x faster                                                        |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                       |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                       |
| genshi_text              | 31.8 ms                                                | 23.9 ms: 1.33x faster                                                       |
| pylint                   | 551 ms                                                 | 416 ms: 1.33x faster                                                        |
| tornado_http             | 136 ms                                                 | 103 ms: 1.32x faster                                                        |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                       |
| html5lib                 | 88.9 ms                                                | 69.1 ms: 1.29x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 77.8 ms: 1.28x faster                                                       |
| django_template          | 48.2 ms                                                | 37.9 ms: 1.27x faster                                                       |
| nqueens                  | 106 ms                                                 | 83.8 ms: 1.26x faster                                                       |
| regex_compile            | 188 ms                                                 | 151 ms: 1.25x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.27 sec: 1.24x faster                                                      |
| 2to3                     | 348 ms                                                 | 285 ms: 1.22x faster                                                        |
| sqlglot_normalize        | 143 ms                                                 | 119 ms: 1.20x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 98.7 ms: 1.17x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 846 us: 1.17x faster                                                        |
| sqlglot_optimize         | 69.2 ms                                                | 60.1 ms: 1.15x faster                                                       |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 74.1 ms: 1.14x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 24.6 ms: 1.13x faster                                                       |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.12x faster                                                        |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                                      |
| json_loads               | 31.2 us                                                | 28.5 us: 1.09x faster                                                       |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.08x faster                                                       |
| sympy_str                | 346 ms                                                 | 319 ms: 1.08x faster                                                        |
| json                     | 5.69 ms                                                | 5.27 ms: 1.08x faster                                                       |
| sympy_expand             | 566 ms                                                 | 530 ms: 1.07x faster                                                        |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 63.5 ms: 1.04x faster                                                       |
| sympy_sum                | 196 ms                                                 | 189 ms: 1.04x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 24.9 ms: 1.04x faster                                                       |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                        |
| docutils                 | 3.30 sec                                               | 3.25 sec: 1.01x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                        |
| unpickle_list            | 5.20 us                                                | 5.29 us: 1.02x slower                                                       |
| async_generators         | 444 ms                                                 | 460 ms: 1.04x slower                                                        |
| pickle_list              | 5.08 us                                                | 5.27 us: 1.04x slower                                                       |
| gc_traversal             | 3.62 ms                                                | 3.78 ms: 1.04x slower                                                       |
| unpickle                 | 14.4 us                                                | 15.1 us: 1.05x slower                                                       |
| telco                    | 7.27 ms                                                | 7.83 ms: 1.08x slower                                                       |
| pickle                   | 10.7 us                                                | 11.6 us: 1.09x slower                                                       |
| coverage                 | 79.4 ms                                                | 87.0 ms: 1.09x slower                                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.78 ms: 1.10x slower                                                       |
| pickle_dict              | 29.6 us                                                | 34.1 us: 1.15x slower                                                       |
| python_startup_no_site   | 5.93 ms                                                | 7.17 ms: 1.21x slower                                                       |
| unpack_sequence          | 60.0 ns                                                | 110 ns: 1.83x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.35x faster                                                                |

Benchmark hidden because not significant (2): regex_effbot, bench_mp_pool
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240906-3.14.0a0-7ad3776-JIT/bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.23x