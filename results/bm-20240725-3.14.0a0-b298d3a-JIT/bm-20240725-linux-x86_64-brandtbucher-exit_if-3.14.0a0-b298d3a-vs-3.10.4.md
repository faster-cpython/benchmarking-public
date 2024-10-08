# Results vs. 3.10.4

- fork: brandtbucher
- ref: exit_if
- machine: linux-x86_64
- commit hash: b298d3a
- commit date: 2024-07-25
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 273 ms: 1.28x faster                                           |
| docutils       | 3.30 sec                                               | 2.89 sec: 1.14x faster                                         |
| html5lib       | 88.9 ms                                                | 64.6 ms: 1.37x faster                                          |
| tornado_http   | 136 ms                                                 | 93.5 ms: 1.46x faster                                          |
| Geometric mean | (ref)                                                  | 1.31x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.23x faster                                           |
| async_tree_memoization  | 870 ms                                                 | 418 ms: 2.08x faster                                           |
| async_tree_io           | 1.77 sec                                               | 896 ms: 1.97x faster                                           |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 564 ms: 1.80x faster                                           |
| Geometric mean          | (ref)                                                  | 2.02x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.4 ms: 1.93x faster                                          |
| float          | 117 ms                                                 | 70.8 ms: 1.65x faster                                          |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                           |
| Geometric mean | (ref)                                                  | 1.49x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 135 ms: 1.40x faster                                           |
| regex_v8       | 27.8 ms                                                | 25.8 ms: 1.08x faster                                          |
| regex_effbot   | 3.63 ms                                                | 3.77 ms: 1.04x slower                                          |
| Geometric mean | (ref)                                                  | 1.10x faster                                                   |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 295 us: 1.64x faster                                           |
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.61x faster                                         |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                           |
| xml_etree_process    | 79.1 ms                                                | 56.8 ms: 1.39x faster                                          |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.37x faster                                          |
| xml_etree_generate   | 99.4 ms                                                | 80.8 ms: 1.23x faster                                          |
| xml_etree_iterparse  | 115 ms                                                 | 98.3 ms: 1.17x faster                                          |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                           |
| json_loads           | 31.2 us                                                | 28.1 us: 1.11x faster                                          |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                          |
| python_startup_no_site | 5.93 ms                                                | 7.17 ms: 1.21x slower                                          |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.73 ms: 1.68x faster                                          |
| django_template | 48.2 ms                                                | 35.8 ms: 1.34x faster                                          |
| genshi_text     | 31.8 ms                                                | 24.6 ms: 1.29x faster                                          |
| genshi_xml      | 66.0 ms                                                | 58.4 ms: 1.13x faster                                          |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.22x faster                                           |
| generators               | 80.1 ms                                                | 28.8 ms: 2.78x faster                                          |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.23x faster                                           |
| deltablue                | 7.91 ms                                                | 3.61 ms: 2.19x faster                                          |
| async_tree_memoization   | 870 ms                                                 | 418 ms: 2.08x faster                                           |
| deepcopy_memo            | 58.5 us                                                | 28.7 us: 2.04x faster                                          |
| richards_super           | 94.7 ms                                                | 46.6 ms: 2.03x faster                                          |
| chaos                    | 115 ms                                                 | 57.7 ms: 2.00x faster                                          |
| async_tree_io            | 1.77 sec                                               | 896 ms: 1.97x faster                                           |
| richards                 | 79.3 ms                                                | 40.4 ms: 1.96x faster                                          |
| scimark_monte_carlo      | 118 ms                                                 | 60.9 ms: 1.94x faster                                          |
| nbody                    | 154 ms                                                 | 79.4 ms: 1.93x faster                                          |
| crypto_pyaes             | 128 ms                                                 | 66.5 ms: 1.92x faster                                          |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                           |
| asyncio_tcp              | 922 ms                                                 | 504 ms: 1.83x faster                                           |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 564 ms: 1.80x faster                                           |
| logging_silent           | 190 ns                                                 | 106 ns: 1.80x faster                                           |
| deepcopy                 | 479 us                                                 | 270 us: 1.77x faster                                           |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.75x faster                                          |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.70x faster                                          |
| spectral_norm            | 170 ms                                                 | 100 ms: 1.70x faster                                           |
| scimark_sor              | 220 ms                                                 | 130 ms: 1.69x faster                                           |
| mako                     | 16.3 ms                                                | 9.73 ms: 1.68x faster                                          |
| pyflate                  | 716 ms                                                 | 432 ms: 1.66x faster                                           |
| float                    | 117 ms                                                 | 70.8 ms: 1.65x faster                                          |
| go                       | 240 ms                                                 | 146 ms: 1.64x faster                                           |
| pickle_pure_python       | 484 us                                                 | 295 us: 1.64x faster                                           |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.61x faster                                         |
| sqlglot_transpile        | 2.57 ms                                                | 1.61 ms: 1.60x faster                                          |
| hexiom                   | 10.4 ms                                                | 6.53 ms: 1.59x faster                                          |
| pylint                   | 551 ms                                                 | 350 ms: 1.57x faster                                           |
| scimark_fft              | 466 ms                                                 | 302 ms: 1.54x faster                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.21 ms: 1.54x faster                                          |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                           |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.53x faster                                          |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                          |
| logging_simple           | 8.30 us                                                | 5.60 us: 1.48x faster                                          |
| logging_format           | 9.09 us                                                | 6.18 us: 1.47x faster                                          |
| tornado_http             | 136 ms                                                 | 93.5 ms: 1.46x faster                                          |
| pprint_safe_repr         | 1.02 sec                                               | 710 ms: 1.43x faster                                           |
| fannkuch                 | 532 ms                                                 | 372 ms: 1.43x faster                                           |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                         |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                         |
| regex_compile            | 188 ms                                                 | 135 ms: 1.40x faster                                           |
| xml_etree_process        | 79.1 ms                                                | 56.8 ms: 1.39x faster                                          |
| scimark_lu               | 176 ms                                                 | 127 ms: 1.38x faster                                           |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                          |
| html5lib                 | 88.9 ms                                                | 64.6 ms: 1.37x faster                                          |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.37x faster                                          |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                         |
| django_template          | 48.2 ms                                                | 35.8 ms: 1.34x faster                                          |
| thrift                   | 1.07 ms                                                | 804 us: 1.33x faster                                           |
| genshi_text              | 31.8 ms                                                | 24.6 ms: 1.29x faster                                          |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                          |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.28x faster                                           |
| 2to3                     | 348 ms                                                 | 273 ms: 1.28x faster                                           |
| sqlglot_optimize         | 69.2 ms                                                | 55.7 ms: 1.24x faster                                          |
| nqueens                  | 106 ms                                                 | 85.7 ms: 1.24x faster                                          |
| xml_etree_generate       | 99.4 ms                                                | 80.8 ms: 1.23x faster                                          |
| dulwich_log              | 84.3 ms                                                | 68.5 ms: 1.23x faster                                          |
| dask                     | 441 ms                                                 | 362 ms: 1.22x faster                                           |
| bench_thread_pool        | 986 us                                                 | 824 us: 1.20x faster                                           |
| xml_etree_iterparse      | 115 ms                                                 | 98.3 ms: 1.17x faster                                          |
| sympy_str                | 346 ms                                                 | 296 ms: 1.17x faster                                           |
| sympy_sum                | 196 ms                                                 | 168 ms: 1.17x faster                                           |
| sympy_integrate          | 25.8 ms                                                | 22.2 ms: 1.16x faster                                          |
| docutils                 | 3.30 sec                                               | 2.89 sec: 1.14x faster                                         |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                           |
| sympy_expand             | 566 ms                                                 | 499 ms: 1.13x faster                                           |
| genshi_xml               | 66.0 ms                                                | 58.4 ms: 1.13x faster                                          |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                           |
| mdp                      | 2.85 sec                                               | 2.53 sec: 1.13x faster                                         |
| json_loads               | 31.2 us                                                | 28.1 us: 1.11x faster                                          |
| json                     | 5.69 ms                                                | 5.25 ms: 1.08x faster                                          |
| regex_v8                 | 27.8 ms                                                | 25.8 ms: 1.08x faster                                          |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                           |
| gc_traversal             | 3.62 ms                                                | 3.58 ms: 1.01x faster                                          |
| async_generators         | 444 ms                                                 | 453 ms: 1.02x slower                                           |
| regex_effbot             | 3.63 ms                                                | 3.77 ms: 1.04x slower                                          |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                          |
| telco                    | 7.27 ms                                                | 7.95 ms: 1.09x slower                                          |
| coverage                 | 79.4 ms                                                | 91.4 ms: 1.15x slower                                          |
| python_startup_no_site   | 5.93 ms                                                | 7.17 ms: 1.21x slower                                          |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                   |

Benchmark hidden because not significant (3): bench_mp_pool, asyncio_websockets, regex_dna
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240725-3.14.0a0-b298d3a-JIT/bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.20x