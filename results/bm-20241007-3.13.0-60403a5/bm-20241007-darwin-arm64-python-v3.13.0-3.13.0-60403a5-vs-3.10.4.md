# Results vs. 3.10.4

- fork: python
- ref: v3.13.0
- machine: darwin-arm64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.16x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: 0.59x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 178 ms: 1.08x faster                                   |
| chameleon      | 6.26 ms                                                | 5.08 ms: 1.23x faster                                  |
| docutils       | 1.73 sec                                               | 1.44 sec: 1.20x faster                                 |
| html5lib       | 42.4 ms                                                | 36.6 ms: 1.16x faster                                  |
| Geometric mean | (ref)                                                  | 1.16x faster                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_io           | 980 ms                                                 | 507 ms: 1.93x faster                                   |
| async_tree_none         | 388 ms                                                 | 212 ms: 1.83x faster                                   |
| async_tree_memoization  | 474 ms                                                 | 270 ms: 1.75x faster                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 460 ms: 1.41x faster                                   |
| Geometric mean          | (ref)                                                  | 1.72x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 73.9 ms: 1.26x faster                                  |
| float          | 69.0 ms                                                | 56.2 ms: 1.23x faster                                  |
| pidigits       | 282 ms                                                 | 284 ms: 1.00x slower                                   |
| Geometric mean | (ref)                                                  | 1.15x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 78.5 ms: 1.21x faster                                  |
| regex_dna      | 174 ms                                                 | 148 ms: 1.18x faster                                   |
| regex_v8       | 17.1 ms                                                | 16.9 ms: 1.01x faster                                  |
| regex_effbot   | 2.46 ms                                                | 2.63 ms: 1.07x slower                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 213 us: 1.32x faster                                   |
| json_dumps           | 8.11 ms                                                | 6.56 ms: 1.24x faster                                  |
| unpickle_pure_python | 194 us                                                 | 163 us: 1.19x faster                                   |
| xml_etree_process    | 46.5 ms                                                | 40.9 ms: 1.14x faster                                  |
| tomli_loads          | 1.71 sec                                               | 1.56 sec: 1.10x faster                                 |
| xml_etree_parse      | 108 ms                                                 | 109 ms: 1.01x slower                                   |
| json_loads           | 16.4 us                                                | 16.9 us: 1.03x slower                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 74.2 ms: 1.03x slower                                  |
| unpickle             | 8.80 us                                                | 9.15 us: 1.04x slower                                  |
| pickle               | 6.97 us                                                | 7.36 us: 1.06x slower                                  |
| xml_etree_generate   | 53.5 ms                                                | 56.6 ms: 1.06x slower                                  |
| pickle_dict          | 17.0 us                                                | 18.2 us: 1.07x slower                                  |
| unpickle_list        | 2.69 us                                                | 2.93 us: 1.09x slower                                  |
| pickle_list          | 2.74 us                                                | 2.99 us: 1.09x slower                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 17.0 ms: 1.57x slower                                  |
| python_startup_no_site | 7.91 ms                                                | 13.7 ms: 1.73x slower                                  |
| Geometric mean         | (ref)                                                  | 1.64x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.68 ms: 1.29x faster                                  |
| django_template | 26.4 ms                                                | 22.2 ms: 1.19x faster                                  |
| genshi_text     | 17.3 ms                                                | 16.9 ms: 1.03x faster                                  |
| genshi_xml      | 33.8 ms                                                | 34.4 ms: 1.02x slower                                  |
| Geometric mean  | (ref)                                                  | 1.11x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 101 us: 3.20x faster                                   |
| async_tree_io            | 980 ms                                                 | 507 ms: 1.93x faster                                   |
| async_tree_none          | 388 ms                                                 | 212 ms: 1.83x faster                                   |
| deltablue                | 4.91 ms                                                | 2.68 ms: 1.83x faster                                  |
| async_tree_memoization   | 474 ms                                                 | 270 ms: 1.75x faster                                   |
| asyncio_websockets       | 410 ms                                                 | 241 ms: 1.70x faster                                   |
| logging_silent           | 117 ns                                                 | 69.9 ns: 1.68x faster                                  |
| raytrace                 | 301 ms                                                 | 182 ms: 1.66x faster                                   |
| chaos                    | 65.8 ms                                                | 41.3 ms: 1.59x faster                                  |
| mypy2                    | 607 ms                                                 | 396 ms: 1.53x faster                                   |
| pylint                   | 277 ms                                                 | 181 ms: 1.53x faster                                   |
| richards_super           | 57.8 ms                                                | 39.1 ms: 1.48x faster                                  |
| sqlglot_parse            | 1.24 ms                                                | 856 us: 1.45x faster                                   |
| asyncio_tcp              | 659 ms                                                 | 457 ms: 1.44x faster                                   |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 460 ms: 1.41x faster                                   |
| sqlglot_transpile        | 1.44 ms                                                | 1.02 ms: 1.41x faster                                  |
| comprehensions           | 16.9 us                                                | 12.2 us: 1.39x faster                                  |
| richards                 | 48.7 ms                                                | 35.4 ms: 1.37x faster                                  |
| scimark_lu               | 103 ms                                                 | 76.5 ms: 1.34x faster                                  |
| crypto_pyaes             | 71.8 ms                                                | 54.0 ms: 1.33x faster                                  |
| pickle_pure_python       | 281 us                                                 | 213 us: 1.32x faster                                   |
| go                       | 151 ms                                                 | 115 ms: 1.31x faster                                   |
| scimark_monte_carlo      | 65.6 ms                                                | 50.4 ms: 1.30x faster                                  |
| mako                     | 9.87 ms                                                | 7.68 ms: 1.29x faster                                  |
| hexiom                   | 6.19 ms                                                | 4.85 ms: 1.28x faster                                  |
| deepcopy_memo            | 34.7 us                                                | 27.2 us: 1.28x faster                                  |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.26 sec: 1.27x faster                                 |
| nbody                    | 93.0 ms                                                | 73.9 ms: 1.26x faster                                  |
| logging_format           | 4.83 us                                                | 3.85 us: 1.25x faster                                  |
| logging_simple           | 4.45 us                                                | 3.57 us: 1.24x faster                                  |
| pycparser                | 877 ms                                                 | 706 ms: 1.24x faster                                   |
| json_dumps               | 8.11 ms                                                | 6.56 ms: 1.24x faster                                  |
| chameleon                | 6.26 ms                                                | 5.08 ms: 1.23x faster                                  |
| dulwich_log              | 35.3 ms                                                | 28.7 ms: 1.23x faster                                  |
| thrift                   | 572 us                                                 | 466 us: 1.23x faster                                   |
| spectral_norm            | 94.8 ms                                                | 77.3 ms: 1.23x faster                                  |
| float                    | 69.0 ms                                                | 56.2 ms: 1.23x faster                                  |
| sympy_sum                | 92.2 ms                                                | 75.6 ms: 1.22x faster                                  |
| pyflate                  | 427 ms                                                 | 351 ms: 1.22x faster                                   |
| regex_compile            | 95.3 ms                                                | 78.5 ms: 1.21x faster                                  |
| scimark_sor              | 128 ms                                                 | 106 ms: 1.21x faster                                   |
| pprint_pformat           | 1.30 sec                                               | 1.08 sec: 1.21x faster                                 |
| pprint_safe_repr         | 641 ms                                                 | 531 ms: 1.21x faster                                   |
| docutils                 | 1.73 sec                                               | 1.44 sec: 1.20x faster                                 |
| unpickle_pure_python     | 194 us                                                 | 163 us: 1.19x faster                                   |
| django_template          | 26.4 ms                                                | 22.2 ms: 1.19x faster                                  |
| regex_dna                | 174 ms                                                 | 148 ms: 1.18x faster                                   |
| deepcopy                 | 272 us                                                 | 232 us: 1.17x faster                                   |
| sympy_integrate          | 13.1 ms                                                | 11.3 ms: 1.16x faster                                  |
| html5lib                 | 42.4 ms                                                | 36.6 ms: 1.16x faster                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.99 ms: 1.14x faster                                  |
| xml_etree_process        | 46.5 ms                                                | 40.9 ms: 1.14x faster                                  |
| sympy_str                | 165 ms                                                 | 145 ms: 1.14x faster                                   |
| deepcopy_reduce          | 2.33 us                                                | 2.06 us: 1.13x faster                                  |
| scimark_fft              | 224 ms                                                 | 201 ms: 1.12x faster                                   |
| tomli_loads              | 1.71 sec                                               | 1.56 sec: 1.10x faster                                 |
| sympy_expand             | 269 ms                                                 | 246 ms: 1.09x faster                                   |
| mdp                      | 1.63 sec                                               | 1.50 sec: 1.09x faster                                 |
| unpack_sequence          | 39.0 ns                                                | 36.1 ns: 1.08x faster                                  |
| 2to3                     | 192 ms                                                 | 178 ms: 1.08x faster                                   |
| pathlib                  | 24.5 ms                                                | 22.8 ms: 1.07x faster                                  |
| fannkuch                 | 303 ms                                                 | 282 ms: 1.07x faster                                   |
| create_gc_cycles         | 860 us                                                 | 803 us: 1.07x faster                                   |
| meteor_contest           | 77.7 ms                                                | 73.8 ms: 1.05x faster                                  |
| sqlglot_optimize         | 36.8 ms                                                | 34.9 ms: 1.05x faster                                  |
| json                     | 3.08 ms                                                | 2.94 ms: 1.05x faster                                  |
| coroutines               | 20.7 ms                                                | 19.8 ms: 1.05x faster                                  |
| bench_thread_pool        | 527 us                                                 | 506 us: 1.04x faster                                   |
| genshi_text              | 17.3 ms                                                | 16.9 ms: 1.03x faster                                  |
| generators               | 32.3 ms                                                | 31.5 ms: 1.03x faster                                  |
| nqueens                  | 63.8 ms                                                | 62.9 ms: 1.01x faster                                  |
| regex_v8                 | 17.1 ms                                                | 16.9 ms: 1.01x faster                                  |
| sqlglot_normalize        | 190 ms                                                 | 189 ms: 1.01x faster                                   |
| pidigits                 | 282 ms                                                 | 284 ms: 1.00x slower                                   |
| xml_etree_parse          | 108 ms                                                 | 109 ms: 1.01x slower                                   |
| genshi_xml               | 33.8 ms                                                | 34.4 ms: 1.02x slower                                  |
| json_loads               | 16.4 us                                                | 16.9 us: 1.03x slower                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 74.2 ms: 1.03x slower                                  |
| unpickle                 | 8.80 us                                                | 9.15 us: 1.04x slower                                  |
| gc_traversal             | 2.36 ms                                                | 2.48 ms: 1.05x slower                                  |
| pickle                   | 6.97 us                                                | 7.36 us: 1.06x slower                                  |
| sqlite_synth             | 1.46 us                                                | 1.54 us: 1.06x slower                                  |
| xml_etree_generate       | 53.5 ms                                                | 56.6 ms: 1.06x slower                                  |
| regex_effbot             | 2.46 ms                                                | 2.63 ms: 1.07x slower                                  |
| pickle_dict              | 17.0 us                                                | 18.2 us: 1.07x slower                                  |
| unpickle_list            | 2.69 us                                                | 2.93 us: 1.09x slower                                  |
| flaskblogging            | 2.65 ms                                                | 2.89 ms: 1.09x slower                                  |
| pickle_list              | 2.74 us                                                | 2.99 us: 1.09x slower                                  |
| coverage                 | 41.5 ms                                                | 46.1 ms: 1.11x slower                                  |
| async_generators         | 231 ms                                                 | 294 ms: 1.27x slower                                   |
| bench_mp_pool            | 37.4 ms                                                | 50.9 ms: 1.36x slower                                  |
| telco                    | 3.49 ms                                                | 4.80 ms: 1.38x slower                                  |
| python_startup           | 10.9 ms                                                | 17.0 ms: 1.57x slower                                  |
| python_startup_no_site   | 7.91 ms                                                | 13.7 ms: 1.73x slower                                  |
| Geometric mean           | (ref)                                                  | 1.16x faster                                           |

Benchmark hidden because not significant (4): tornado_http, dask, gunicorn, aiohttp
Ignored benchmarks (2) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: 0.59x