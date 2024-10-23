# Results vs. 3.10.4

- fork: brandtbucher
- ref: jump_backward_0
- machine: linux-x86_64
- commit hash: d0d3a27
- commit date: 2024-10-23
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.38x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 288 ms: 1.21x faster                                                    |
| docutils       | 3.30 sec                                               | 3.41 sec: 1.03x slower                                                  |
| html5lib       | 88.9 ms                                                | 70.3 ms: 1.26x faster                                                   |
| tornado_http   | 136 ms                                                 | 112 ms: 1.22x faster                                                    |
| Geometric mean | (ref)                                                  | 1.16x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 350 ms: 2.08x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 434 ms: 2.01x faster                                                    |
| async_tree_io           | 1.77 sec                                               | 940 ms: 1.88x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 596 ms: 1.71x faster                                                    |
| Geometric mean          | (ref)                                                  | 1.91x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.2 ms: 1.89x faster                                                   |
| float          | 117 ms                                                 | 75.5 ms: 1.55x faster                                                   |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                  | 1.44x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 147 ms: 1.28x faster                                                    |
| regex_v8       | 27.8 ms                                                | 26.1 ms: 1.07x faster                                                   |
| regex_dna      | 227 ms                                                 | 223 ms: 1.02x faster                                                    |
| regex_effbot   | 3.63 ms                                                | 3.94 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 296 us: 1.64x faster                                                    |
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 226 us: 1.46x faster                                                    |
| xml_etree_process    | 79.1 ms                                                | 59.8 ms: 1.32x faster                                                   |
| json_dumps           | 14.2 ms                                                | 11.0 ms: 1.29x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 82.8 ms: 1.20x faster                                                   |
| json_loads           | 31.2 us                                                | 26.7 us: 1.17x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 99.4 ms: 1.16x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                    |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.9 ms: 1.22x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 7.22 ms: 1.22x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.5 ms: 1.56x faster                                                   |
| genshi_text     | 31.8 ms                                                | 26.6 ms: 1.20x faster                                                   |
| django_template | 48.2 ms                                                | 40.5 ms: 1.19x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 62.8 ms: 1.05x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.24x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.25x faster                                                    |
| generators               | 80.1 ms                                                | 36.5 ms: 2.20x faster                                                   |
| async_tree_none          | 728 ms                                                 | 350 ms: 2.08x faster                                                    |
| async_tree_memoization   | 870 ms                                                 | 434 ms: 2.01x faster                                                    |
| deltablue                | 7.91 ms                                                | 4.03 ms: 1.96x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 30.1 us: 1.94x faster                                                   |
| chaos                    | 115 ms                                                 | 59.5 ms: 1.94x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 62.3 ms: 1.90x faster                                                   |
| nbody                    | 154 ms                                                 | 81.2 ms: 1.89x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 940 ms: 1.88x faster                                                    |
| crypto_pyaes             | 128 ms                                                 | 68.3 ms: 1.87x faster                                                   |
| go                       | 240 ms                                                 | 129 ms: 1.86x faster                                                    |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                    |
| logging_silent           | 190 ns                                                 | 108 ns: 1.76x faster                                                    |
| deepcopy                 | 479 us                                                 | 276 us: 1.74x faster                                                    |
| raytrace                 | 507 ms                                                 | 295 ms: 1.72x faster                                                    |
| richards_super           | 94.7 ms                                                | 55.2 ms: 1.72x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 596 ms: 1.71x faster                                                    |
| pickle_pure_python       | 484 us                                                 | 296 us: 1.64x faster                                                    |
| comprehensions           | 28.8 us                                                | 17.8 us: 1.61x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                  |
| richards                 | 79.3 ms                                                | 49.9 ms: 1.59x faster                                                   |
| mako                     | 16.3 ms                                                | 10.5 ms: 1.56x faster                                                   |
| float                    | 117 ms                                                 | 75.5 ms: 1.55x faster                                                   |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.54x faster                                                    |
| pyflate                  | 716 ms                                                 | 467 ms: 1.53x faster                                                    |
| sqlglot_parse            | 2.17 ms                                                | 1.44 ms: 1.51x faster                                                   |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.47x faster                                                    |
| unpickle_pure_python     | 331 us                                                 | 226 us: 1.46x faster                                                    |
| scimark_fft              | 466 ms                                                 | 319 ms: 1.46x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.91 us: 1.43x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 715 ms: 1.42x faster                                                    |
| fannkuch                 | 532 ms                                                 | 378 ms: 1.41x faster                                                    |
| hexiom                   | 10.4 ms                                                | 7.48 ms: 1.39x faster                                                   |
| sqlglot_transpile        | 2.57 ms                                                | 1.85 ms: 1.39x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.66 ms: 1.39x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 59.8 ms: 1.32x faster                                                   |
| coroutines               | 35.1 ms                                                | 26.6 ms: 1.32x faster                                                   |
| thrift                   | 1.07 ms                                                | 826 us: 1.30x faster                                                    |
| json_dumps               | 14.2 ms                                                | 11.0 ms: 1.29x faster                                                   |
| regex_compile            | 188 ms                                                 | 147 ms: 1.28x faster                                                    |
| html5lib                 | 88.9 ms                                                | 70.3 ms: 1.26x faster                                                   |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 68.6 ms: 1.23x faster                                                   |
| logging_format           | 9.09 us                                                | 7.43 us: 1.22x faster                                                   |
| python_startup           | 14.6 ms                                                | 11.9 ms: 1.22x faster                                                   |
| tornado_http             | 136 ms                                                 | 112 ms: 1.22x faster                                                    |
| nqueens                  | 106 ms                                                 | 87.3 ms: 1.21x faster                                                   |
| 2to3                     | 348 ms                                                 | 288 ms: 1.21x faster                                                    |
| logging_simple           | 8.30 us                                                | 6.90 us: 1.20x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 82.8 ms: 1.20x faster                                                   |
| genshi_text              | 31.8 ms                                                | 26.6 ms: 1.20x faster                                                   |
| django_template          | 48.2 ms                                                | 40.5 ms: 1.19x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 121 ms: 1.18x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.34 sec: 1.18x faster                                                  |
| pylint                   | 551 ms                                                 | 468 ms: 1.18x faster                                                    |
| json_loads               | 31.2 us                                                | 26.7 us: 1.17x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 99.4 ms: 1.16x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                    |
| json                     | 5.69 ms                                                | 4.97 ms: 1.14x faster                                                   |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.10x faster                                                    |
| mdp                      | 2.85 sec                                               | 2.65 sec: 1.07x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 26.1 ms: 1.07x faster                                                   |
| sympy_expand             | 566 ms                                                 | 536 ms: 1.05x faster                                                    |
| genshi_xml               | 66.0 ms                                                | 62.8 ms: 1.05x faster                                                   |
| sympy_str                | 346 ms                                                 | 333 ms: 1.04x faster                                                    |
| sqlglot_optimize         | 69.2 ms                                                | 67.2 ms: 1.03x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 963 us: 1.02x faster                                                    |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                    |
| regex_dna                | 227 ms                                                 | 223 ms: 1.02x faster                                                    |
| docutils                 | 3.30 sec                                               | 3.41 sec: 1.03x slower                                                  |
| telco                    | 7.27 ms                                                | 7.64 ms: 1.05x slower                                                   |
| async_generators         | 444 ms                                                 | 468 ms: 1.05x slower                                                    |
| sympy_sum                | 196 ms                                                 | 208 ms: 1.06x slower                                                    |
| sympy_integrate          | 25.8 ms                                                | 27.6 ms: 1.07x slower                                                   |
| regex_effbot             | 3.63 ms                                                | 3.94 ms: 1.08x slower                                                   |
| coverage                 | 79.4 ms                                                | 86.9 ms: 1.09x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 7.22 ms: 1.22x slower                                                   |
| gc_traversal             | 3.62 ms                                                | 4.85 ms: 1.34x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 2.69 ms: 1.66x slower                                                   |
| bench_mp_pool            | 24.0 ms                                                | 89.9 ms: 3.74x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                            |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241023-3.14.0a1+-d0d3a27-JIT/bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.38x