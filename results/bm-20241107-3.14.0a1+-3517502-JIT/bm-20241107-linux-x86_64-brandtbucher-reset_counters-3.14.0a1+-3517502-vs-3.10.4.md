# Results vs. 3.10.4

- fork: brandtbucher
- ref: reset_counters
- machine: linux-x86_64
- commit hash: 3517502
- commit date: 2024-11-07
- overall geometric mean: 1.382x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 280 ms: 1.24x faster                                                   |
| docutils       | 3.30 sec                                               | 2.92 sec: 1.13x faster                                                 |
| html5lib       | 88.9 ms                                                | 65.4 ms: 1.36x faster                                                  |
| Geometric mean | (ref)                                                  | 1.24x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 331 ms: 2.20x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 414 ms: 2.10x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 859 ms: 2.06x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 573 ms: 1.77x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.03x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.4 ms: 1.86x faster                                                  |
| float          | 117 ms                                                 | 76.6 ms: 1.53x faster                                                  |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.43x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 140 ms: 1.34x faster                                                   |
| regex_v8       | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                  |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                                   |
| pickle_pure_python   | 484 us                                                 | 327 us: 1.48x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 55.8 ms: 1.42x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.0 ms: 1.29x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 79.2 ms: 1.26x faster                                                  |
| json_loads           | 31.2 us                                                | 26.6 us: 1.17x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.15x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.13x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.12 ms: 1.20x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.2 ms: 1.60x faster                                                  |
| django_template | 48.2 ms                                                | 36.1 ms: 1.33x faster                                                  |
| genshi_text     | 31.8 ms                                                | 25.9 ms: 1.23x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 61.9 ms: 1.07x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.29x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.21x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.29 ms: 2.40x faster                                                  |
| generators               | 80.1 ms                                                | 35.9 ms: 2.23x faster                                                  |
| async_tree_none          | 728 ms                                                 | 331 ms: 2.20x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 414 ms: 2.10x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 859 ms: 2.06x faster                                                   |
| richards_super           | 94.7 ms                                                | 48.2 ms: 1.96x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.9 us: 1.96x faster                                                  |
| chaos                    | 115 ms                                                 | 59.5 ms: 1.94x faster                                                  |
| richards                 | 79.3 ms                                                | 41.1 ms: 1.93x faster                                                  |
| logging_silent           | 190 ns                                                 | 100 ns: 1.89x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 68.6 ms: 1.86x faster                                                  |
| nbody                    | 154 ms                                                 | 82.4 ms: 1.86x faster                                                  |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.84x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 64.4 ms: 1.84x faster                                                  |
| raytrace                 | 507 ms                                                 | 278 ms: 1.82x faster                                                   |
| deepcopy                 | 479 us                                                 | 267 us: 1.79x faster                                                   |
| go                       | 240 ms                                                 | 134 ms: 1.79x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 573 ms: 1.77x faster                                                   |
| comprehensions           | 28.8 us                                                | 17.1 us: 1.68x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                 |
| mako                     | 16.3 ms                                                | 10.2 ms: 1.60x faster                                                  |
| pyflate                  | 716 ms                                                 | 451 ms: 1.59x faster                                                   |
| coroutines               | 35.1 ms                                                | 22.4 ms: 1.57x faster                                                  |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.55x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.55x faster                                                  |
| float                    | 117 ms                                                 | 76.6 ms: 1.53x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.69 ms: 1.52x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.59 us: 1.49x faster                                                  |
| logging_format           | 9.09 us                                                | 6.13 us: 1.48x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 327 us: 1.48x faster                                                   |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.48x faster                                                   |
| hexiom                   | 10.4 ms                                                | 7.07 ms: 1.47x faster                                                  |
| scimark_fft              | 466 ms                                                 | 317 ms: 1.47x faster                                                   |
| pylint                   | 551 ms                                                 | 378 ms: 1.46x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.51 ms: 1.43x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 55.8 ms: 1.42x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.53 sec: 1.38x faster                                                 |
| thrift                   | 1.07 ms                                                | 782 us: 1.37x faster                                                   |
| fannkuch                 | 532 ms                                                 | 388 ms: 1.37x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                 |
| html5lib                 | 88.9 ms                                                | 65.4 ms: 1.36x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 749 ms: 1.36x faster                                                   |
| regex_compile            | 188 ms                                                 | 140 ms: 1.34x faster                                                   |
| django_template          | 48.2 ms                                                | 36.1 ms: 1.33x faster                                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.8 ms: 1.31x faster                                                  |
| json_dumps               | 14.2 ms                                                | 11.0 ms: 1.29x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 79.2 ms: 1.26x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.25x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 67.7 ms: 1.25x faster                                                  |
| 2to3                     | 348 ms                                                 | 280 ms: 1.24x faster                                                   |
| genshi_text              | 31.8 ms                                                | 25.9 ms: 1.23x faster                                                  |
| nqueens                  | 106 ms                                                 | 88.0 ms: 1.20x faster                                                  |
| json_loads               | 31.2 us                                                | 26.6 us: 1.17x faster                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 148 ms: 1.16x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 59.6 ms: 1.16x faster                                                  |
| sympy_str                | 346 ms                                                 | 301 ms: 1.15x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.15x faster                                                   |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.13x faster                                                   |
| sympy_sum                | 196 ms                                                 | 174 ms: 1.13x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.92 sec: 1.13x faster                                                 |
| sympy_expand             | 566 ms                                                 | 503 ms: 1.12x faster                                                   |
| json                     | 5.69 ms                                                | 5.06 ms: 1.12x faster                                                  |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                                   |
| sympy_integrate          | 25.8 ms                                                | 23.3 ms: 1.11x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 891 us: 1.11x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.78 us: 1.09x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 61.9 ms: 1.07x faster                                                  |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.76 sec: 1.03x faster                                                 |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                   |
| async_generators         | 444 ms                                                 | 457 ms: 1.03x slower                                                   |
| telco                    | 7.27 ms                                                | 7.60 ms: 1.05x slower                                                  |
| coverage                 | 79.4 ms                                                | 85.7 ms: 1.08x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.12 ms: 1.20x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.67 ms: 1.29x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.69 ms: 1.66x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 84.6 ms: 3.52x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.36x faster                                                           |

Benchmark hidden because not significant (2): asyncio_websockets, regex_effbot
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241107-3.14.0a1+-3517502-JIT/bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.382x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.33x