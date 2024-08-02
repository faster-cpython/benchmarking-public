# Results vs. 3.10.4

- fork: python
- ref: e83ce850f433fd8bbf8f
- machine: darwin-arm64
- commit hash: e83ce85
- commit date: 2024-06-05
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 0.86x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 170 ms: 1.13x faster                                                  |
| docutils       | 1.73 sec                                               | 1.50 sec: 1.15x faster                                                |
| html5lib       | 42.4 ms                                                | 30.9 ms: 1.37x faster                                                 |
| tornado_http   | 86.7 ms                                                | 67.1 ms: 1.29x faster                                                 |
| Geometric mean | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 215 ms: 1.81x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 263 ms: 1.80x faster                                                  |
| async_tree_io           | 980 ms                                                 | 571 ms: 1.72x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 473 ms: 1.37x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.67x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 64.0 ms: 1.45x faster                                                 |
| float          | 69.0 ms                                                | 47.7 ms: 1.45x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.28x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 72.4 ms: 1.32x faster                                                 |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                                  |
| regex_v8       | 17.1 ms                                                | 17.4 ms: 1.02x slower                                                 |
| regex_effbot   | 2.46 ms                                                | 2.56 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 172 us: 1.64x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 132 us: 1.48x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.25 sec: 1.37x faster                                                |
| xml_etree_process    | 46.5 ms                                                | 35.6 ms: 1.31x faster                                                 |
| json_dumps           | 8.11 ms                                                | 6.32 ms: 1.28x faster                                                 |
| xml_etree_generate   | 53.5 ms                                                | 51.1 ms: 1.05x faster                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 70.1 ms: 1.03x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.03x faster                                                  |
| json_loads           | 16.4 us                                                | 17.0 us: 1.03x slower                                                 |
| unpickle             | 8.80 us                                                | 9.30 us: 1.06x slower                                                 |
| unpickle_list        | 2.69 us                                                | 2.85 us: 1.06x slower                                                 |
| pickle               | 6.97 us                                                | 7.45 us: 1.07x slower                                                 |
| pickle_list          | 2.74 us                                                | 2.94 us: 1.07x slower                                                 |
| pickle_dict          | 17.0 us                                                | 18.2 us: 1.07x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 15.4 ms: 1.42x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 12.7 ms: 1.60x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.51x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.36 ms: 1.55x faster                                                 |
| django_template | 26.4 ms                                                | 21.5 ms: 1.23x faster                                                 |
| genshi_text     | 17.3 ms                                                | 16.9 ms: 1.02x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 39.3 ms: 1.16x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 95.3 us: 3.39x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.47 ms: 1.99x faster                                                 |
| logging_silent           | 117 ns                                                 | 63.8 ns: 1.84x faster                                                 |
| raytrace                 | 301 ms                                                 | 164 ms: 1.84x faster                                                  |
| async_tree_none          | 388 ms                                                 | 215 ms: 1.81x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 263 ms: 1.80x faster                                                  |
| async_tree_io            | 980 ms                                                 | 571 ms: 1.72x faster                                                  |
| chaos                    | 65.8 ms                                                | 39.7 ms: 1.66x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 172 us: 1.64x faster                                                  |
| deepcopy_memo            | 34.7 us                                                | 21.3 us: 1.63x faster                                                 |
| richards_super           | 57.8 ms                                                | 35.6 ms: 1.62x faster                                                 |
| mako                     | 9.87 ms                                                | 6.36 ms: 1.55x faster                                                 |
| richards                 | 48.7 ms                                                | 31.6 ms: 1.54x faster                                                 |
| pylint                   | 277 ms                                                 | 183 ms: 1.51x faster                                                  |
| sqlglot_parse            | 1.24 ms                                                | 830 us: 1.50x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 132 us: 1.48x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 44.5 ms: 1.47x faster                                                 |
| go                       | 151 ms                                                 | 102 ms: 1.47x faster                                                  |
| nbody                    | 93.0 ms                                                | 64.0 ms: 1.45x faster                                                 |
| float                    | 69.0 ms                                                | 47.7 ms: 1.45x faster                                                 |
| asyncio_tcp              | 659 ms                                                 | 457 ms: 1.44x faster                                                  |
| logging_simple           | 4.45 us                                                | 3.10 us: 1.44x faster                                                 |
| sqlglot_transpile        | 1.44 ms                                                | 1.01 ms: 1.43x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 67.3 ms: 1.41x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.41 ms: 1.40x faster                                                 |
| logging_format           | 4.83 us                                                | 3.44 us: 1.40x faster                                                 |
| pprint_safe_repr         | 641 ms                                                 | 460 ms: 1.39x faster                                                  |
| crypto_pyaes             | 71.8 ms                                                | 51.8 ms: 1.39x faster                                                 |
| generators               | 32.3 ms                                                | 23.5 ms: 1.38x faster                                                 |
| pprint_pformat           | 1.30 sec                                               | 947 ms: 1.38x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 473 ms: 1.37x faster                                                  |
| comprehensions           | 16.9 us                                                | 12.3 us: 1.37x faster                                                 |
| html5lib                 | 42.4 ms                                                | 30.9 ms: 1.37x faster                                                 |
| tomli_loads              | 1.71 sec                                               | 1.25 sec: 1.37x faster                                                |
| pyflate                  | 427 ms                                                 | 314 ms: 1.36x faster                                                  |
| thrift                   | 572 us                                                 | 434 us: 1.32x faster                                                  |
| deepcopy                 | 272 us                                                 | 206 us: 1.32x faster                                                  |
| regex_compile            | 95.3 ms                                                | 72.4 ms: 1.32x faster                                                 |
| coroutines               | 20.7 ms                                                | 15.8 ms: 1.31x faster                                                 |
| xml_etree_process        | 46.5 ms                                                | 35.6 ms: 1.31x faster                                                 |
| scimark_lu               | 103 ms                                                 | 79.1 ms: 1.30x faster                                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.23 sec: 1.30x faster                                                |
| pycparser                | 877 ms                                                 | 677 ms: 1.29x faster                                                  |
| tornado_http             | 86.7 ms                                                | 67.1 ms: 1.29x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.32 ms: 1.28x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.82 us: 1.28x faster                                                 |
| sympy_sum                | 92.2 ms                                                | 72.6 ms: 1.27x faster                                                 |
| fannkuch                 | 303 ms                                                 | 239 ms: 1.27x faster                                                  |
| scimark_sor              | 128 ms                                                 | 102 ms: 1.26x faster                                                  |
| django_template          | 26.4 ms                                                | 21.5 ms: 1.23x faster                                                 |
| scimark_fft              | 224 ms                                                 | 185 ms: 1.21x faster                                                  |
| sympy_integrate          | 13.1 ms                                                | 10.9 ms: 1.20x faster                                                 |
| sympy_str                | 165 ms                                                 | 139 ms: 1.19x faster                                                  |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.95 ms: 1.16x faster                                                 |
| docutils                 | 1.73 sec                                               | 1.50 sec: 1.15x faster                                                |
| dask                     | 253 ms                                                 | 222 ms: 1.14x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.44 sec: 1.13x faster                                                |
| 2to3                     | 192 ms                                                 | 170 ms: 1.13x faster                                                  |
| sympy_expand             | 269 ms                                                 | 239 ms: 1.13x faster                                                  |
| pathlib                  | 24.5 ms                                                | 21.9 ms: 1.12x faster                                                 |
| sqlglot_optimize         | 36.8 ms                                                | 33.2 ms: 1.11x faster                                                 |
| bench_thread_pool        | 527 us                                                 | 483 us: 1.09x faster                                                  |
| nqueens                  | 63.8 ms                                                | 58.9 ms: 1.08x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 72.5 ms: 1.07x faster                                                 |
| json                     | 3.08 ms                                                | 2.93 ms: 1.05x faster                                                 |
| xml_etree_generate       | 53.5 ms                                                | 51.1 ms: 1.05x faster                                                 |
| xml_etree_iterparse      | 72.1 ms                                                | 70.1 ms: 1.03x faster                                                 |
| xml_etree_parse          | 108 ms                                                 | 105 ms: 1.03x faster                                                  |
| genshi_text              | 17.3 ms                                                | 16.9 ms: 1.02x faster                                                 |
| pidigits                 | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 17.4 ms: 1.02x slower                                                 |
| json_loads               | 16.4 us                                                | 17.0 us: 1.03x slower                                                 |
| regex_effbot             | 2.46 ms                                                | 2.56 ms: 1.04x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.47 ms: 1.05x slower                                                 |
| unpickle                 | 8.80 us                                                | 9.30 us: 1.06x slower                                                 |
| unpickle_list            | 2.69 us                                                | 2.85 us: 1.06x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 914 us: 1.06x slower                                                  |
| pickle                   | 6.97 us                                                | 7.45 us: 1.07x slower                                                 |
| sqlite_synth             | 1.46 us                                                | 1.56 us: 1.07x slower                                                 |
| pickle_list              | 2.74 us                                                | 2.94 us: 1.07x slower                                                 |
| pickle_dict              | 17.0 us                                                | 18.2 us: 1.07x slower                                                 |
| coverage                 | 41.5 ms                                                | 45.6 ms: 1.10x slower                                                 |
| genshi_xml               | 33.8 ms                                                | 39.3 ms: 1.16x slower                                                 |
| async_generators         | 231 ms                                                 | 289 ms: 1.25x slower                                                  |
| telco                    | 3.49 ms                                                | 4.47 ms: 1.28x slower                                                 |
| bench_mp_pool            | 37.4 ms                                                | 49.4 ms: 1.32x slower                                                 |
| python_startup           | 10.9 ms                                                | 15.4 ms: 1.42x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 12.7 ms: 1.60x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.23x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (12) of results/bm-20240605-3.14.0a0-e83ce85-JIT/bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 0.86x