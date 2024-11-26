# Results vs. 3.10.4

- fork: brandtbucher
- ref: jb0_invalidate
- machine: linux-x86_64
- commit hash: 69e9a0e
- commit date: 2024-10-24
- overall geometric mean: 1.321x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.39x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 284 ms: 1.23x faster                                                   |
| docutils       | 3.30 sec                                               | 3.36 sec: 1.02x slower                                                 |
| html5lib       | 88.9 ms                                                | 69.9 ms: 1.27x faster                                                  |
| tornado_http   | 136 ms                                                 | 112 ms: 1.22x faster                                                   |
| Geometric mean | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 347 ms: 2.10x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 434 ms: 2.00x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 950 ms: 1.86x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 599 ms: 1.70x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.91x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.4 ms: 1.86x faster                                                  |
| float          | 117 ms                                                 | 75.3 ms: 1.56x faster                                                  |
| pidigits       | 191 ms                                                 | 188 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.43x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 147 ms: 1.28x faster                                                   |
| regex_v8       | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                  |
| regex_dna      | 227 ms                                                 | 220 ms: 1.03x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.74 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 295 us: 1.64x faster                                                   |
| tomli_loads          | 3.14 sec                                               | 1.99 sec: 1.58x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 225 us: 1.47x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 59.8 ms: 1.32x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.27x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 83.2 ms: 1.20x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 99.4 ms: 1.16x faster                                                  |
| json_loads           | 31.2 us                                                | 27.0 us: 1.16x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.9 ms: 1.22x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.22 ms: 1.22x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.6 ms: 1.54x faster                                                  |
| genshi_text     | 31.8 ms                                                | 26.2 ms: 1.22x faster                                                  |
| django_template | 48.2 ms                                                | 40.1 ms: 1.20x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 62.9 ms: 1.05x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.24x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.29x faster                                                   |
| generators               | 80.1 ms                                                | 36.7 ms: 2.18x faster                                                  |
| async_tree_none          | 728 ms                                                 | 347 ms: 2.10x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 434 ms: 2.00x faster                                                   |
| deltablue                | 7.91 ms                                                | 4.04 ms: 1.96x faster                                                  |
| chaos                    | 115 ms                                                 | 59.4 ms: 1.94x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 30.2 us: 1.94x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 62.4 ms: 1.90x faster                                                  |
| nbody                    | 154 ms                                                 | 82.4 ms: 1.86x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 950 ms: 1.86x faster                                                   |
| go                       | 240 ms                                                 | 129 ms: 1.86x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 69.1 ms: 1.85x faster                                                  |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.81x faster                                                   |
| logging_silent           | 190 ns                                                 | 109 ns: 1.74x faster                                                   |
| deepcopy                 | 479 us                                                 | 275 us: 1.74x faster                                                   |
| richards_super           | 94.7 ms                                                | 55.4 ms: 1.71x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 599 ms: 1.70x faster                                                   |
| raytrace                 | 507 ms                                                 | 299 ms: 1.70x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 295 us: 1.64x faster                                                   |
| comprehensions           | 28.8 us                                                | 17.9 us: 1.61x faster                                                  |
| richards                 | 79.3 ms                                                | 49.6 ms: 1.60x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.99 sec: 1.58x faster                                                 |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                   |
| float                    | 117 ms                                                 | 75.3 ms: 1.56x faster                                                  |
| mako                     | 16.3 ms                                                | 10.6 ms: 1.54x faster                                                  |
| pyflate                  | 716 ms                                                 | 466 ms: 1.54x faster                                                   |
| sqlglot_parse            | 2.17 ms                                                | 1.43 ms: 1.52x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 225 us: 1.47x faster                                                   |
| spectral_norm            | 170 ms                                                 | 116 ms: 1.47x faster                                                   |
| scimark_fft              | 466 ms                                                 | 319 ms: 1.46x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.87 us: 1.45x faster                                                  |
| hexiom                   | 10.4 ms                                                | 7.17 ms: 1.45x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 723 ms: 1.41x faster                                                   |
| fannkuch                 | 532 ms                                                 | 378 ms: 1.41x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.85 ms: 1.39x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.73 ms: 1.37x faster                                                  |
| coroutines               | 35.1 ms                                                | 26.5 ms: 1.32x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 59.8 ms: 1.32x faster                                                  |
| thrift                   | 1.07 ms                                                | 829 us: 1.29x faster                                                   |
| regex_compile            | 188 ms                                                 | 147 ms: 1.28x faster                                                   |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.27x faster                                                  |
| html5lib                 | 88.9 ms                                                | 69.9 ms: 1.27x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 68.7 ms: 1.23x faster                                                  |
| 2to3                     | 348 ms                                                 | 284 ms: 1.23x faster                                                   |
| python_startup           | 14.6 ms                                                | 11.9 ms: 1.22x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.8 ms: 1.22x faster                                                  |
| tornado_http             | 136 ms                                                 | 112 ms: 1.22x faster                                                   |
| genshi_text              | 31.8 ms                                                | 26.2 ms: 1.22x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.31 sec: 1.21x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 119 ms: 1.20x faster                                                   |
| django_template          | 48.2 ms                                                | 40.1 ms: 1.20x faster                                                  |
| pylint                   | 551 ms                                                 | 460 ms: 1.20x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 83.2 ms: 1.20x faster                                                  |
| logging_format           | 9.09 us                                                | 7.61 us: 1.20x faster                                                  |
| nqueens                  | 106 ms                                                 | 89.3 ms: 1.18x faster                                                  |
| logging_simple           | 8.30 us                                                | 7.01 us: 1.18x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 99.4 ms: 1.16x faster                                                  |
| json_loads               | 31.2 us                                                | 27.0 us: 1.16x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                                   |
| json                     | 5.69 ms                                                | 5.08 ms: 1.12x faster                                                  |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 65.1 ms: 1.06x faster                                                  |
| sympy_expand             | 566 ms                                                 | 536 ms: 1.05x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 62.9 ms: 1.05x faster                                                  |
| sympy_str                | 346 ms                                                 | 335 ms: 1.03x faster                                                   |
| regex_dna                | 227 ms                                                 | 220 ms: 1.03x faster                                                   |
| sqlalchemy_imperative    | 23.3 ms                                                | 22.7 ms: 1.03x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 967 us: 1.02x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.81 sec: 1.01x faster                                                 |
| pidigits                 | 191 ms                                                 | 188 ms: 1.01x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 174 ms: 1.01x slower                                                   |
| docutils                 | 3.30 sec                                               | 3.36 sec: 1.02x slower                                                 |
| sympy_integrate          | 25.8 ms                                                | 26.5 ms: 1.03x slower                                                  |
| regex_effbot             | 3.63 ms                                                | 3.74 ms: 1.03x slower                                                  |
| async_generators         | 444 ms                                                 | 462 ms: 1.04x slower                                                   |
| telco                    | 7.27 ms                                                | 7.62 ms: 1.05x slower                                                  |
| sympy_sum                | 196 ms                                                 | 209 ms: 1.07x slower                                                   |
| coverage                 | 79.4 ms                                                | 86.9 ms: 1.09x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.22 ms: 1.22x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.55 ms: 1.26x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.69 ms: 1.66x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 89.3 ms: 3.72x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241024-3.14.0a1+-69e9a0e-JIT/bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.321x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.39x