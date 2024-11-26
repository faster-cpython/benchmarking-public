# Results vs. 3.10.4

- fork: brandtbucher
- ref: tier_two_exit_leaks
- machine: linux-x86_64
- commit hash: 984ca75
- commit date: 2024-10-01
- overall geometric mean: 1.418x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 279 ms: 1.25x faster                                                       |
| docutils       | 3.30 sec                                               | 2.92 sec: 1.13x faster                                                     |
| html5lib       | 88.9 ms                                                | 66.2 ms: 1.34x faster                                                      |
| tornado_http   | 136 ms                                                 | 95.7 ms: 1.42x faster                                                      |
| Geometric mean | (ref)                                                  | 1.28x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 321 ms: 2.27x faster                                                       |
| async_tree_memoization  | 870 ms                                                 | 410 ms: 2.12x faster                                                       |
| async_tree_io           | 1.77 sec                                               | 891 ms: 1.98x faster                                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 576 ms: 1.77x faster                                                       |
| Geometric mean          | (ref)                                                  | 2.03x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.5 ms: 1.91x faster                                                      |
| float          | 117 ms                                                 | 72.3 ms: 1.62x faster                                                      |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.47x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 143 ms: 1.32x faster                                                       |
| regex_v8       | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                      |
| regex_dna      | 227 ms                                                 | 222 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                  | 1.11x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                     |
| pickle_pure_python   | 484 us                                                 | 310 us: 1.56x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 55.2 ms: 1.43x faster                                                      |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                      |
| xml_etree_generate   | 99.4 ms                                                | 77.7 ms: 1.28x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 97.5 ms: 1.18x faster                                                      |
| json_loads           | 31.2 us                                                | 26.7 us: 1.17x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 145 ms: 1.16x faster                                                       |
| pickle_list          | 5.08 us                                                | 5.18 us: 1.02x slower                                                      |
| unpickle             | 14.4 us                                                | 14.7 us: 1.02x slower                                                      |
| unpickle_list        | 5.20 us                                                | 5.33 us: 1.03x slower                                                      |
| pickle               | 10.7 us                                                | 11.7 us: 1.09x slower                                                      |
| pickle_dict          | 29.6 us                                                | 34.7 us: 1.17x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                      |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.87 ms: 1.65x faster                                                      |
| django_template | 48.2 ms                                                | 36.0 ms: 1.34x faster                                                      |
| genshi_text     | 31.8 ms                                                | 25.3 ms: 1.26x faster                                                      |
| genshi_xml      | 66.0 ms                                                | 59.2 ms: 1.12x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.30x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.21 ms: 2.47x faster                                                      |
| generators               | 80.1 ms                                                | 34.9 ms: 2.29x faster                                                      |
| async_tree_none          | 728 ms                                                 | 321 ms: 2.27x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 27.0 us: 2.17x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 410 ms: 2.12x faster                                                       |
| richards_super           | 94.7 ms                                                | 45.1 ms: 2.10x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 891 ms: 1.98x faster                                                       |
| richards                 | 79.3 ms                                                | 40.0 ms: 1.98x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 65.7 ms: 1.95x faster                                                      |
| chaos                    | 115 ms                                                 | 60.0 ms: 1.92x faster                                                      |
| nbody                    | 154 ms                                                 | 80.5 ms: 1.91x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 62.5 ms: 1.89x faster                                                      |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                                       |
| asyncio_tcp              | 922 ms                                                 | 494 ms: 1.86x faster                                                       |
| raytrace                 | 507 ms                                                 | 276 ms: 1.83x faster                                                       |
| go                       | 240 ms                                                 | 132 ms: 1.82x faster                                                       |
| logging_silent           | 190 ns                                                 | 105 ns: 1.81x faster                                                       |
| deepcopy                 | 479 us                                                 | 271 us: 1.77x faster                                                       |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 576 ms: 1.77x faster                                                       |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.72x faster                                                      |
| mako                     | 16.3 ms                                                | 9.87 ms: 1.65x faster                                                      |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.65x faster                                                       |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                     |
| float                    | 117 ms                                                 | 72.3 ms: 1.62x faster                                                      |
| scimark_lu               | 176 ms                                                 | 109 ms: 1.61x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.35 ms: 1.61x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 310 us: 1.56x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                                      |
| pyflate                  | 716 ms                                                 | 462 ms: 1.55x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                                       |
| scimark_fft              | 466 ms                                                 | 307 ms: 1.52x faster                                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.70 ms: 1.52x faster                                                      |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.51x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.92 ms: 1.50x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.54 us: 1.50x faster                                                      |
| logging_format           | 9.09 us                                                | 6.08 us: 1.49x faster                                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.37 ms: 1.48x faster                                                      |
| pylint                   | 551 ms                                                 | 374 ms: 1.47x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 55.2 ms: 1.43x faster                                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                     |
| tornado_http             | 136 ms                                                 | 95.7 ms: 1.42x faster                                                      |
| fannkuch                 | 532 ms                                                 | 376 ms: 1.41x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 735 ms: 1.39x faster                                                       |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                      |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.36x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.35x faster                                                     |
| html5lib                 | 88.9 ms                                                | 66.2 ms: 1.34x faster                                                      |
| django_template          | 48.2 ms                                                | 36.0 ms: 1.34x faster                                                      |
| thrift                   | 1.07 ms                                                | 809 us: 1.33x faster                                                       |
| regex_compile            | 188 ms                                                 | 143 ms: 1.32x faster                                                       |
| pathlib                  | 20.5 ms                                                | 15.7 ms: 1.31x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 77.7 ms: 1.28x faster                                                      |
| genshi_text              | 31.8 ms                                                | 25.3 ms: 1.26x faster                                                      |
| 2to3                     | 348 ms                                                 | 279 ms: 1.25x faster                                                       |
| dulwich_log              | 84.3 ms                                                | 67.8 ms: 1.24x faster                                                      |
| sqlglot_normalize        | 143 ms                                                 | 117 ms: 1.22x faster                                                       |
| nqueens                  | 106 ms                                                 | 88.6 ms: 1.19x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 97.5 ms: 1.18x faster                                                      |
| json_loads               | 31.2 us                                                | 26.7 us: 1.17x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 145 ms: 1.16x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 60.5 ms: 1.14x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                      |
| sympy_str                | 346 ms                                                 | 305 ms: 1.13x faster                                                       |
| json                     | 5.69 ms                                                | 5.02 ms: 1.13x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.92 sec: 1.13x faster                                                     |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 59.2 ms: 1.12x faster                                                      |
| sympy_expand             | 566 ms                                                 | 508 ms: 1.11x faster                                                       |
| sympy_sum                | 196 ms                                                 | 176 ms: 1.11x faster                                                       |
| sqlite_synth             | 3.02 us                                                | 2.74 us: 1.10x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 894 us: 1.10x faster                                                       |
| sympy_integrate          | 25.8 ms                                                | 23.5 ms: 1.10x faster                                                      |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                       |
| regex_dna                | 227 ms                                                 | 222 ms: 1.02x faster                                                       |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                       |
| pickle_list              | 5.08 us                                                | 5.18 us: 1.02x slower                                                      |
| unpickle                 | 14.4 us                                                | 14.7 us: 1.02x slower                                                      |
| unpickle_list            | 5.20 us                                                | 5.33 us: 1.03x slower                                                      |
| async_generators         | 444 ms                                                 | 457 ms: 1.03x slower                                                       |
| telco                    | 7.27 ms                                                | 7.49 ms: 1.03x slower                                                      |
| create_gc_cycles         | 1.62 ms                                                | 1.73 ms: 1.07x slower                                                      |
| coverage                 | 79.4 ms                                                | 85.3 ms: 1.07x slower                                                      |
| pickle                   | 10.7 us                                                | 11.7 us: 1.09x slower                                                      |
| gc_traversal             | 3.62 ms                                                | 3.99 ms: 1.10x slower                                                      |
| pickle_dict              | 29.6 us                                                | 34.7 us: 1.17x slower                                                      |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                      |
| unpack_sequence          | 60.0 ns                                                | 108 ns: 1.80x slower                                                       |
| bench_mp_pool            | 24.0 ms                                                | 60.7 ms: 2.53x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.36x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241001-3.14.0a0-984ca75-JIT/bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.418x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.18x