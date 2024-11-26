# Results vs. 3.10.4

- fork: brandtbucher
- ref: ujb0_project_warmup
- machine: linux-x86_64
- commit hash: f67fedc
- commit date: 2024-09-09
- overall geometric mean: 1.353x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 292 ms: 1.19x faster                                                       |
| docutils       | 3.30 sec                                               | 3.47 sec: 1.05x slower                                                     |
| html5lib       | 88.9 ms                                                | 70.6 ms: 1.26x faster                                                      |
| tornado_http   | 136 ms                                                 | 119 ms: 1.14x faster                                                       |
| Geometric mean | (ref)                                                  | 1.13x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 339 ms: 2.15x faster                                                       |
| async_tree_memoization  | 870 ms                                                 | 422 ms: 2.06x faster                                                       |
| async_tree_io           | 1.77 sec                                               | 947 ms: 1.87x faster                                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 571 ms: 1.78x faster                                                       |
| Geometric mean          | (ref)                                                  | 1.96x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.2 ms: 1.87x faster                                                      |
| float          | 117 ms                                                 | 69.9 ms: 1.68x faster                                                      |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.48x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 155 ms: 1.22x faster                                                       |
| regex_v8       | 27.8 ms                                                | 25.9 ms: 1.07x faster                                                      |
| regex_dna      | 227 ms                                                 | 215 ms: 1.05x faster                                                       |
| regex_effbot   | 3.63 ms                                                | 3.77 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                  | 1.07x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 191 us: 1.73x faster                                                       |
| pickle_pure_python   | 484 us                                                 | 314 us: 1.54x faster                                                       |
| tomli_loads          | 3.14 sec                                               | 2.06 sec: 1.52x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 54.0 ms: 1.46x faster                                                      |
| json_dumps           | 14.2 ms                                                | 9.90 ms: 1.43x faster                                                      |
| xml_etree_generate   | 99.4 ms                                                | 78.1 ms: 1.27x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 98.2 ms: 1.18x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 144 ms: 1.17x faster                                                       |
| json_loads           | 31.2 us                                                | 29.5 us: 1.06x faster                                                      |
| unpickle             | 14.4 us                                                | 14.7 us: 1.02x slower                                                      |
| unpickle_list        | 5.20 us                                                | 5.31 us: 1.02x slower                                                      |
| pickle_list          | 5.08 us                                                | 5.19 us: 1.02x slower                                                      |
| pickle               | 10.7 us                                                | 11.4 us: 1.07x slower                                                      |
| pickle_dict          | 29.6 us                                                | 35.2 us: 1.19x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.8 ms: 1.36x faster                                                      |
| python_startup_no_site | 5.93 ms                                                | 7.19 ms: 1.21x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.65 ms: 1.69x faster                                                      |
| genshi_text     | 31.8 ms                                                | 22.6 ms: 1.41x faster                                                      |
| django_template | 48.2 ms                                                | 38.8 ms: 1.24x faster                                                      |
| genshi_xml      | 66.0 ms                                                | 59.0 ms: 1.12x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.32x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.29 ms: 2.41x faster                                                      |
| generators               | 80.1 ms                                                | 34.8 ms: 2.30x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 27.1 us: 2.16x faster                                                      |
| async_tree_none          | 728 ms                                                 | 339 ms: 2.15x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 422 ms: 2.06x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 58.1 ms: 2.03x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 68.2 ms: 1.87x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 947 ms: 1.87x faster                                                       |
| nbody                    | 154 ms                                                 | 82.2 ms: 1.87x faster                                                      |
| chaos                    | 115 ms                                                 | 62.3 ms: 1.85x faster                                                      |
| raytrace                 | 507 ms                                                 | 275 ms: 1.84x faster                                                       |
| logging_silent           | 190 ns                                                 | 103 ns: 1.84x faster                                                       |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.81x faster                                                       |
| deepcopy                 | 479 us                                                 | 267 us: 1.80x faster                                                       |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 571 ms: 1.78x faster                                                       |
| asyncio_tcp              | 922 ms                                                 | 522 ms: 1.77x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 191 us: 1.73x faster                                                       |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                                      |
| mako                     | 16.3 ms                                                | 9.65 ms: 1.69x faster                                                      |
| float                    | 117 ms                                                 | 69.9 ms: 1.68x faster                                                      |
| scimark_lu               | 176 ms                                                 | 109 ms: 1.61x faster                                                       |
| spectral_norm            | 170 ms                                                 | 107 ms: 1.58x faster                                                       |
| richards_super           | 94.7 ms                                                | 60.8 ms: 1.56x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 314 us: 1.54x faster                                                       |
| tomli_loads              | 3.14 sec                                               | 2.06 sec: 1.52x faster                                                     |
| pyflate                  | 716 ms                                                 | 471 ms: 1.52x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.79 us: 1.50x faster                                                      |
| scimark_fft              | 466 ms                                                 | 312 ms: 1.49x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.38 ms: 1.48x faster                                                      |
| richards                 | 79.3 ms                                                | 53.8 ms: 1.47x faster                                                      |
| coroutines               | 35.1 ms                                                | 23.9 ms: 1.47x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 54.0 ms: 1.46x faster                                                      |
| hexiom                   | 10.4 ms                                                | 7.14 ms: 1.46x faster                                                      |
| json_dumps               | 14.2 ms                                                | 9.90 ms: 1.43x faster                                                      |
| fannkuch                 | 532 ms                                                 | 372 ms: 1.43x faster                                                       |
| logging_simple           | 8.30 us                                                | 5.88 us: 1.41x faster                                                      |
| logging_format           | 9.09 us                                                | 6.43 us: 1.41x faster                                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.82 sec: 1.41x faster                                                     |
| genshi_text              | 31.8 ms                                                | 22.6 ms: 1.41x faster                                                      |
| python_startup           | 14.6 ms                                                | 10.8 ms: 1.36x faster                                                      |
| go                       | 240 ms                                                 | 178 ms: 1.35x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 761 ms: 1.34x faster                                                       |
| thrift                   | 1.07 ms                                                | 809 us: 1.33x faster                                                       |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 78.1 ms: 1.27x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.66 sec: 1.27x faster                                                     |
| nqueens                  | 106 ms                                                 | 84.0 ms: 1.26x faster                                                      |
| html5lib                 | 88.9 ms                                                | 70.6 ms: 1.26x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.73 ms: 1.26x faster                                                      |
| django_template          | 48.2 ms                                                | 38.8 ms: 1.24x faster                                                      |
| regex_compile            | 188 ms                                                 | 155 ms: 1.22x faster                                                       |
| pycparser                | 1.58 sec                                               | 1.30 sec: 1.21x faster                                                     |
| 2to3                     | 348 ms                                                 | 292 ms: 1.19x faster                                                       |
| sqlglot_transpile        | 2.57 ms                                                | 2.17 ms: 1.19x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 98.2 ms: 1.18x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 144 ms: 1.17x faster                                                       |
| pylint                   | 551 ms                                                 | 480 ms: 1.15x faster                                                       |
| sqlglot_normalize        | 143 ms                                                 | 125 ms: 1.15x faster                                                       |
| tornado_http             | 136 ms                                                 | 119 ms: 1.14x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 59.0 ms: 1.12x faster                                                      |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.10x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 898 us: 1.10x faster                                                       |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                                      |
| json                     | 5.69 ms                                                | 5.29 ms: 1.08x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 25.9 ms: 1.07x faster                                                      |
| json_loads               | 31.2 us                                                | 29.5 us: 1.06x faster                                                      |
| regex_dna                | 227 ms                                                 | 215 ms: 1.05x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.72 sec: 1.05x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 67.1 ms: 1.03x faster                                                      |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                       |
| sympy_expand             | 566 ms                                                 | 556 ms: 1.02x faster                                                       |
| sympy_str                | 346 ms                                                 | 341 ms: 1.01x faster                                                       |
| unpickle                 | 14.4 us                                                | 14.7 us: 1.02x slower                                                      |
| unpickle_list            | 5.20 us                                                | 5.31 us: 1.02x slower                                                      |
| pickle_list              | 5.08 us                                                | 5.19 us: 1.02x slower                                                      |
| async_generators         | 444 ms                                                 | 455 ms: 1.02x slower                                                       |
| regex_effbot             | 3.63 ms                                                | 3.77 ms: 1.04x slower                                                      |
| gc_traversal             | 3.62 ms                                                | 3.78 ms: 1.04x slower                                                      |
| docutils                 | 3.30 sec                                               | 3.47 sec: 1.05x slower                                                     |
| sympy_integrate          | 25.8 ms                                                | 27.3 ms: 1.06x slower                                                      |
| pickle                   | 10.7 us                                                | 11.4 us: 1.07x slower                                                      |
| telco                    | 7.27 ms                                                | 7.75 ms: 1.07x slower                                                      |
| coverage                 | 79.4 ms                                                | 85.4 ms: 1.08x slower                                                      |
| sympy_sum                | 196 ms                                                 | 214 ms: 1.09x slower                                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.79 ms: 1.10x slower                                                      |
| pickle_dict              | 29.6 us                                                | 35.2 us: 1.19x slower                                                      |
| python_startup_no_site   | 5.93 ms                                                | 7.19 ms: 1.21x slower                                                      |
| unpack_sequence          | 60.0 ns                                                | 148 ns: 2.47x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.31x faster                                                               |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240909-3.14.0a0-f67fedc-JIT/bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.353x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.31x