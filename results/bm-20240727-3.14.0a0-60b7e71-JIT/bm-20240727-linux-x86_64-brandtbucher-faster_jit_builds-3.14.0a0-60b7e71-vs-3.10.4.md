# Results vs. 3.10.4

- fork: brandtbucher
- ref: faster_jit_builds
- machine: linux-x86_64
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 272 ms: 1.28x faster                                                     |
| docutils       | 3.30 sec                                               | 2.91 sec: 1.13x faster                                                   |
| html5lib       | 88.9 ms                                                | 65.8 ms: 1.35x faster                                                    |
| tornado_http   | 136 ms                                                 | 93.3 ms: 1.46x faster                                                    |
| Geometric mean | (ref)                                                  | 1.30x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 328 ms: 2.22x faster                                                     |
| async_tree_memoization  | 870 ms                                                 | 416 ms: 2.09x faster                                                     |
| async_tree_io           | 1.77 sec                                               | 904 ms: 1.96x faster                                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 568 ms: 1.79x faster                                                     |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.1 ms: 1.92x faster                                                    |
| float          | 117 ms                                                 | 70.6 ms: 1.66x faster                                                    |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.48x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 134 ms: 1.40x faster                                                     |
| regex_v8       | 27.8 ms                                                | 25.8 ms: 1.08x faster                                                    |
| regex_dna      | 227 ms                                                 | 229 ms: 1.01x slower                                                     |
| regex_effbot   | 3.63 ms                                                | 3.82 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                  | 1.09x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 297 us: 1.63x faster                                                     |
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 56.8 ms: 1.39x faster                                                    |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                    |
| xml_etree_generate   | 99.4 ms                                                | 81.3 ms: 1.22x faster                                                    |
| xml_etree_iterparse  | 115 ms                                                 | 100 ms: 1.15x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                                     |
| json_loads           | 31.2 us                                                | 27.8 us: 1.12x faster                                                    |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                    |
| python_startup_no_site | 5.93 ms                                                | 7.17 ms: 1.21x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.82 ms: 1.66x faster                                                    |
| django_template | 48.2 ms                                                | 35.6 ms: 1.35x faster                                                    |
| genshi_text     | 31.8 ms                                                | 24.8 ms: 1.28x faster                                                    |
| genshi_xml      | 66.0 ms                                                | 58.4 ms: 1.13x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.21x faster                                                     |
| generators               | 80.1 ms                                                | 28.8 ms: 2.78x faster                                                    |
| async_tree_none          | 728 ms                                                 | 328 ms: 2.22x faster                                                     |
| deltablue                | 7.91 ms                                                | 3.65 ms: 2.17x faster                                                    |
| async_tree_memoization   | 870 ms                                                 | 416 ms: 2.09x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 28.3 us: 2.07x faster                                                    |
| richards_super           | 94.7 ms                                                | 46.9 ms: 2.02x faster                                                    |
| chaos                    | 115 ms                                                 | 58.5 ms: 1.97x faster                                                    |
| richards                 | 79.3 ms                                                | 40.4 ms: 1.96x faster                                                    |
| async_tree_io            | 1.77 sec                                               | 904 ms: 1.96x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 66.3 ms: 1.93x faster                                                    |
| nbody                    | 154 ms                                                 | 80.1 ms: 1.92x faster                                                    |
| scimark_monte_carlo      | 118 ms                                                 | 61.8 ms: 1.91x faster                                                    |
| raytrace                 | 507 ms                                                 | 270 ms: 1.88x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 498 ms: 1.85x faster                                                     |
| logging_silent           | 190 ns                                                 | 103 ns: 1.84x faster                                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 568 ms: 1.79x faster                                                     |
| deepcopy                 | 479 us                                                 | 273 us: 1.75x faster                                                     |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                    |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.70x faster                                                    |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.69x faster                                                     |
| scimark_sor              | 220 ms                                                 | 130 ms: 1.69x faster                                                     |
| mako                     | 16.3 ms                                                | 9.82 ms: 1.66x faster                                                    |
| float                    | 117 ms                                                 | 70.6 ms: 1.66x faster                                                    |
| pickle_pure_python       | 484 us                                                 | 297 us: 1.63x faster                                                     |
| pyflate                  | 716 ms                                                 | 439 ms: 1.63x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                   |
| go                       | 240 ms                                                 | 149 ms: 1.61x faster                                                     |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                                    |
| hexiom                   | 10.4 ms                                                | 6.59 ms: 1.58x faster                                                    |
| pylint                   | 551 ms                                                 | 351 ms: 1.57x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                     |
| logging_simple           | 8.30 us                                                | 5.46 us: 1.52x faster                                                    |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                    |
| logging_format           | 9.09 us                                                | 6.03 us: 1.51x faster                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.30 ms: 1.51x faster                                                    |
| deepcopy_reduce          | 4.17 us                                                | 2.81 us: 1.48x faster                                                    |
| scimark_fft              | 466 ms                                                 | 316 ms: 1.48x faster                                                     |
| tornado_http             | 136 ms                                                 | 93.3 ms: 1.46x faster                                                    |
| fannkuch                 | 532 ms                                                 | 367 ms: 1.45x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 707 ms: 1.44x faster                                                     |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                   |
| regex_compile            | 188 ms                                                 | 134 ms: 1.40x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 56.8 ms: 1.39x faster                                                    |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                    |
| scimark_lu               | 176 ms                                                 | 128 ms: 1.37x faster                                                     |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                    |
| django_template          | 48.2 ms                                                | 35.6 ms: 1.35x faster                                                    |
| html5lib                 | 88.9 ms                                                | 65.8 ms: 1.35x faster                                                    |
| thrift                   | 1.07 ms                                                | 800 us: 1.34x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                                   |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                    |
| genshi_text              | 31.8 ms                                                | 24.8 ms: 1.28x faster                                                    |
| 2to3                     | 348 ms                                                 | 272 ms: 1.28x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.25x faster                                                     |
| nqueens                  | 106 ms                                                 | 86.0 ms: 1.23x faster                                                    |
| sqlglot_optimize         | 69.2 ms                                                | 56.2 ms: 1.23x faster                                                    |
| xml_etree_generate       | 99.4 ms                                                | 81.3 ms: 1.22x faster                                                    |
| dask                     | 441 ms                                                 | 365 ms: 1.21x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 826 us: 1.19x faster                                                     |
| sympy_str                | 346 ms                                                 | 294 ms: 1.17x faster                                                     |
| sympy_sum                | 196 ms                                                 | 169 ms: 1.16x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 22.3 ms: 1.16x faster                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 100 ms: 1.15x faster                                                     |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.91 sec: 1.13x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 58.4 ms: 1.13x faster                                                    |
| sympy_expand             | 566 ms                                                 | 501 ms: 1.13x faster                                                     |
| json_loads               | 31.2 us                                                | 27.8 us: 1.12x faster                                                    |
| json                     | 5.69 ms                                                | 5.17 ms: 1.10x faster                                                    |
| mdp                      | 2.85 sec                                               | 2.60 sec: 1.10x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 25.8 ms: 1.08x faster                                                    |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                     |
| regex_dna                | 227 ms                                                 | 229 ms: 1.01x slower                                                     |
| async_generators         | 444 ms                                                 | 452 ms: 1.02x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 3.78 ms: 1.04x slower                                                    |
| regex_effbot             | 3.63 ms                                                | 3.82 ms: 1.05x slower                                                    |
| telco                    | 7.27 ms                                                | 7.84 ms: 1.08x slower                                                    |
| create_gc_cycles         | 1.62 ms                                                | 1.77 ms: 1.09x slower                                                    |
| coverage                 | 79.4 ms                                                | 93.0 ms: 1.17x slower                                                    |
| python_startup_no_site   | 5.93 ms                                                | 7.17 ms: 1.21x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240727-3.14.0a0-60b7e71-JIT/bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.20x