# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 1e7db3e
- commit date: 2024-07-29
- overall geometric mean: 1.39x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 289 ms: 1.21x faster                                                      |
| docutils       | 3.30 sec                                               | 3.09 sec: 1.07x faster                                                    |
| html5lib       | 88.9 ms                                                | 67.5 ms: 1.32x faster                                                     |
| tornado_http   | 136 ms                                                 | 94.7 ms: 1.44x faster                                                     |
| Geometric mean | (ref)                                                  | 1.25x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 329 ms: 2.21x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 429 ms: 2.03x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 914 ms: 1.94x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 563 ms: 1.80x faster                                                      |
| Geometric mean          | (ref)                                                  | 1.99x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.1 ms: 1.92x faster                                                     |
| float          | 117 ms                                                 | 71.6 ms: 1.64x faster                                                     |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.48x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 151 ms: 1.25x faster                                                      |
| regex_v8       | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                     |
| regex_dna      | 227 ms                                                 | 225 ms: 1.01x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.70 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                  | 1.09x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 304 us: 1.59x faster                                                      |
| tomli_loads          | 3.14 sec                                               | 1.98 sec: 1.59x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                      |
| json_dumps           | 14.2 ms                                                | 10.2 ms: 1.39x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 57.9 ms: 1.37x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 82.0 ms: 1.21x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.15x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.14x faster                                                      |
| json_loads           | 31.2 us                                                | 27.9 us: 1.12x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.13 ms: 1.20x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.63 ms: 1.70x faster                                                     |
| genshi_text     | 31.8 ms                                                | 24.6 ms: 1.29x faster                                                     |
| django_template | 48.2 ms                                                | 38.0 ms: 1.27x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 56.2 ms: 1.18x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 176 us: 3.08x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.08 ms: 2.57x faster                                                     |
| generators               | 80.1 ms                                                | 34.1 ms: 2.35x faster                                                     |
| async_tree_none          | 728 ms                                                 | 329 ms: 2.21x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 27.9 us: 2.09x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 429 ms: 2.03x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 914 ms: 1.94x faster                                                      |
| chaos                    | 115 ms                                                 | 60.0 ms: 1.92x faster                                                     |
| nbody                    | 154 ms                                                 | 80.1 ms: 1.92x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 67.0 ms: 1.91x faster                                                     |
| logging_silent           | 190 ns                                                 | 101 ns: 1.88x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 63.7 ms: 1.86x faster                                                     |
| richards_super           | 94.7 ms                                                | 51.3 ms: 1.85x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 507 ms: 1.82x faster                                                      |
| raytrace                 | 507 ms                                                 | 281 ms: 1.80x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 563 ms: 1.80x faster                                                      |
| richards                 | 79.3 ms                                                | 44.7 ms: 1.77x faster                                                     |
| deepcopy                 | 479 us                                                 | 271 us: 1.77x faster                                                      |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.70x faster                                                     |
| mako                     | 16.3 ms                                                | 9.63 ms: 1.70x faster                                                     |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.66x faster                                                      |
| scimark_sor              | 220 ms                                                 | 134 ms: 1.64x faster                                                      |
| float                    | 117 ms                                                 | 71.6 ms: 1.64x faster                                                     |
| sqlglot_parse            | 2.17 ms                                                | 1.34 ms: 1.62x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 304 us: 1.59x faster                                                      |
| pyflate                  | 716 ms                                                 | 450 ms: 1.59x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 1.98 sec: 1.59x faster                                                    |
| go                       | 240 ms                                                 | 152 ms: 1.58x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                                     |
| coroutines               | 35.1 ms                                                | 22.4 ms: 1.56x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.71 ms: 1.51x faster                                                     |
| logging_simple           | 8.30 us                                                | 5.57 us: 1.49x faster                                                     |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                                      |
| logging_format           | 9.09 us                                                | 6.12 us: 1.48x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.42 ms: 1.46x faster                                                     |
| tornado_http             | 136 ms                                                 | 94.7 ms: 1.44x faster                                                     |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                    |
| fannkuch                 | 532 ms                                                 | 375 ms: 1.42x faster                                                      |
| pylint                   | 551 ms                                                 | 394 ms: 1.40x faster                                                      |
| json_dumps               | 14.2 ms                                                | 10.2 ms: 1.39x faster                                                     |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 57.9 ms: 1.37x faster                                                     |
| thrift                   | 1.07 ms                                                | 792 us: 1.35x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.56 sec: 1.35x faster                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 757 ms: 1.34x faster                                                      |
| scimark_lu               | 176 ms                                                 | 132 ms: 1.34x faster                                                      |
| html5lib                 | 88.9 ms                                                | 67.5 ms: 1.32x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                                    |
| genshi_text              | 31.8 ms                                                | 24.6 ms: 1.29x faster                                                     |
| hexiom                   | 10.4 ms                                                | 8.07 ms: 1.29x faster                                                     |
| django_template          | 48.2 ms                                                | 38.0 ms: 1.27x faster                                                     |
| regex_compile            | 188 ms                                                 | 151 ms: 1.25x faster                                                      |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 82.0 ms: 1.21x faster                                                     |
| 2to3                     | 348 ms                                                 | 289 ms: 1.21x faster                                                      |
| sqlglot_normalize        | 143 ms                                                 | 119 ms: 1.20x faster                                                      |
| dask                     | 441 ms                                                 | 368 ms: 1.20x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 839 us: 1.18x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 56.2 ms: 1.18x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 60.4 ms: 1.15x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.15x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.14x faster                                                      |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                      |
| json_loads               | 31.2 us                                                | 27.9 us: 1.12x faster                                                     |
| nqueens                  | 106 ms                                                 | 94.6 ms: 1.12x faster                                                     |
| json                     | 5.69 ms                                                | 5.20 ms: 1.09x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.62 sec: 1.09x faster                                                    |
| sympy_str                | 346 ms                                                 | 322 ms: 1.08x faster                                                      |
| docutils                 | 3.30 sec                                               | 3.09 sec: 1.07x faster                                                    |
| sympy_sum                | 196 ms                                                 | 186 ms: 1.06x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 24.8 ms: 1.04x faster                                                     |
| sympy_expand             | 566 ms                                                 | 545 ms: 1.04x faster                                                      |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                      |
| regex_dna                | 227 ms                                                 | 225 ms: 1.01x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                      |
| regex_effbot             | 3.63 ms                                                | 3.70 ms: 1.02x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 3.81 ms: 1.05x slower                                                     |
| async_generators         | 444 ms                                                 | 473 ms: 1.07x slower                                                      |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.09x slower                                                     |
| telco                    | 7.27 ms                                                | 7.98 ms: 1.10x slower                                                     |
| coverage                 | 79.4 ms                                                | 91.6 ms: 1.15x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.13 ms: 1.20x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                              |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240729-3.14.0a0-1e7db3e-JIT/bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.23x