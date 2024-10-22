# Results vs. 3.13.0

- fork: python
- ref: v3.10.4
- machine: darwin-arm64
- commit hash: 9d38120
- commit date: 2022-03-23
- overall geometric mean: 1.16x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x slower
- Memory change: 5.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 192 ms: 1.08x slower                                   |
| chameleon      | 5.08 ms                                                | 6.26 ms: 1.23x slower                                  |
| docutils       | 1.44 sec                                               | 1.73 sec: 1.20x slower                                 |
| html5lib       | 36.6 ms                                                | 42.4 ms: 1.16x slower                                  |
| Geometric mean | (ref)                                                  | 1.16x slower                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_generators        | 294 ms                                                 | 231 ms: 1.27x faster                                   |
| coroutines              | 19.8 ms                                                | 20.7 ms: 1.05x slower                                  |
| asyncio_tcp_ssl         | 1.26 sec                                               | 1.60 sec: 1.27x slower                                 |
| async_tree_cpu_io_mixed | 460 ms                                                 | 649 ms: 1.41x slower                                   |
| asyncio_tcp             | 457 ms                                                 | 659 ms: 1.44x slower                                   |
| asyncio_websockets      | 241 ms                                                 | 410 ms: 1.70x slower                                   |
| async_tree_memoization  | 270 ms                                                 | 474 ms: 1.75x slower                                   |
| async_tree_none         | 212 ms                                                 | 388 ms: 1.83x slower                                   |
| async_tree_io           | 507 ms                                                 | 980 ms: 1.93x slower                                   |
| Geometric mean          | (ref)                                                  | 1.41x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 284 ms                                                 | 282 ms: 1.00x faster                                   |
| float          | 56.2 ms                                                | 69.0 ms: 1.23x slower                                  |
| nbody          | 73.9 ms                                                | 93.0 ms: 1.26x slower                                  |
| Geometric mean | (ref)                                                  | 1.15x slower                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.46 ms: 1.07x faster                                  |
| regex_v8       | 16.9 ms                                                | 17.1 ms: 1.01x slower                                  |
| regex_dna      | 148 ms                                                 | 174 ms: 1.18x slower                                   |
| regex_compile  | 78.5 ms                                                | 95.3 ms: 1.21x slower                                  |
| Geometric mean | (ref)                                                  | 1.08x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_list          | 2.99 us                                                | 2.74 us: 1.09x faster                                  |
| unpickle_list        | 2.93 us                                                | 2.69 us: 1.09x faster                                  |
| pickle_dict          | 18.2 us                                                | 17.0 us: 1.07x faster                                  |
| xml_etree_generate   | 56.6 ms                                                | 53.5 ms: 1.06x faster                                  |
| pickle               | 7.36 us                                                | 6.97 us: 1.06x faster                                  |
| unpickle             | 9.15 us                                                | 8.80 us: 1.04x faster                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 72.1 ms: 1.03x faster                                  |
| json_loads           | 16.9 us                                                | 16.4 us: 1.03x faster                                  |
| xml_etree_parse      | 109 ms                                                 | 108 ms: 1.01x faster                                   |
| tomli_loads          | 1.56 sec                                               | 1.71 sec: 1.10x slower                                 |
| xml_etree_process    | 40.9 ms                                                | 46.5 ms: 1.14x slower                                  |
| unpickle_pure_python | 163 us                                                 | 194 us: 1.19x slower                                   |
| json_dumps           | 6.56 ms                                                | 8.11 ms: 1.24x slower                                  |
| pickle_pure_python   | 213 us                                                 | 281 us: 1.32x slower                                   |
| Geometric mean       | (ref)                                                  | 1.03x slower                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 7.91 ms: 1.73x faster                                  |
| python_startup         | 17.0 ms                                                | 10.9 ms: 1.57x faster                                  |
| Geometric mean         | (ref)                                                  | 1.64x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 34.4 ms                                                | 33.8 ms: 1.02x faster                                  |
| genshi_text     | 16.9 ms                                                | 17.3 ms: 1.03x slower                                  |
| django_template | 22.2 ms                                                | 26.4 ms: 1.19x slower                                  |
| mako            | 7.68 ms                                                | 9.87 ms: 1.29x slower                                  |
| Geometric mean  | (ref)                                                  | 1.11x slower                                           |

All benchmarks:
===============

| Benchmark                | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site   | 13.7 ms                                                | 7.91 ms: 1.73x faster                                  |
| python_startup           | 17.0 ms                                                | 10.9 ms: 1.57x faster                                  |
| telco                    | 4.80 ms                                                | 3.49 ms: 1.38x faster                                  |
| bench_mp_pool            | 50.9 ms                                                | 37.4 ms: 1.36x faster                                  |
| async_generators         | 294 ms                                                 | 231 ms: 1.27x faster                                   |
| coverage                 | 46.1 ms                                                | 41.5 ms: 1.11x faster                                  |
| pickle_list              | 2.99 us                                                | 2.74 us: 1.09x faster                                  |
| flaskblogging            | 2.89 ms                                                | 2.65 ms: 1.09x faster                                  |
| unpickle_list            | 2.93 us                                                | 2.69 us: 1.09x faster                                  |
| pickle_dict              | 18.2 us                                                | 17.0 us: 1.07x faster                                  |
| regex_effbot             | 2.63 ms                                                | 2.46 ms: 1.07x faster                                  |
| xml_etree_generate       | 56.6 ms                                                | 53.5 ms: 1.06x faster                                  |
| sqlite_synth             | 1.54 us                                                | 1.46 us: 1.06x faster                                  |
| pickle                   | 7.36 us                                                | 6.97 us: 1.06x faster                                  |
| gc_traversal             | 2.48 ms                                                | 2.36 ms: 1.05x faster                                  |
| unpickle                 | 9.15 us                                                | 8.80 us: 1.04x faster                                  |
| xml_etree_iterparse      | 74.2 ms                                                | 72.1 ms: 1.03x faster                                  |
| json_loads               | 16.9 us                                                | 16.4 us: 1.03x faster                                  |
| genshi_xml               | 34.4 ms                                                | 33.8 ms: 1.02x faster                                  |
| xml_etree_parse          | 109 ms                                                 | 108 ms: 1.01x faster                                   |
| pidigits                 | 284 ms                                                 | 282 ms: 1.00x faster                                   |
| sqlglot_normalize        | 189 ms                                                 | 190 ms: 1.01x slower                                   |
| regex_v8                 | 16.9 ms                                                | 17.1 ms: 1.01x slower                                  |
| nqueens                  | 62.9 ms                                                | 63.8 ms: 1.01x slower                                  |
| generators               | 31.5 ms                                                | 32.3 ms: 1.03x slower                                  |
| genshi_text              | 16.9 ms                                                | 17.3 ms: 1.03x slower                                  |
| bench_thread_pool        | 506 us                                                 | 527 us: 1.04x slower                                   |
| coroutines               | 19.8 ms                                                | 20.7 ms: 1.05x slower                                  |
| json                     | 2.94 ms                                                | 3.08 ms: 1.05x slower                                  |
| sqlglot_optimize         | 34.9 ms                                                | 36.8 ms: 1.05x slower                                  |
| meteor_contest           | 73.8 ms                                                | 77.7 ms: 1.05x slower                                  |
| create_gc_cycles         | 803 us                                                 | 860 us: 1.07x slower                                   |
| fannkuch                 | 282 ms                                                 | 303 ms: 1.07x slower                                   |
| pathlib                  | 22.8 ms                                                | 24.5 ms: 1.07x slower                                  |
| 2to3                     | 178 ms                                                 | 192 ms: 1.08x slower                                   |
| unpack_sequence          | 36.1 ns                                                | 39.0 ns: 1.08x slower                                  |
| mdp                      | 1.50 sec                                               | 1.63 sec: 1.09x slower                                 |
| sympy_expand             | 246 ms                                                 | 269 ms: 1.09x slower                                   |
| tomli_loads              | 1.56 sec                                               | 1.71 sec: 1.10x slower                                 |
| scimark_fft              | 201 ms                                                 | 224 ms: 1.12x slower                                   |
| deepcopy_reduce          | 2.06 us                                                | 2.33 us: 1.13x slower                                  |
| sympy_str                | 145 ms                                                 | 165 ms: 1.14x slower                                   |
| xml_etree_process        | 40.9 ms                                                | 46.5 ms: 1.14x slower                                  |
| scimark_sparse_mat_mult  | 2.99 ms                                                | 3.42 ms: 1.14x slower                                  |
| html5lib                 | 36.6 ms                                                | 42.4 ms: 1.16x slower                                  |
| sympy_integrate          | 11.3 ms                                                | 13.1 ms: 1.16x slower                                  |
| deepcopy                 | 232 us                                                 | 272 us: 1.17x slower                                   |
| regex_dna                | 148 ms                                                 | 174 ms: 1.18x slower                                   |
| django_template          | 22.2 ms                                                | 26.4 ms: 1.19x slower                                  |
| unpickle_pure_python     | 163 us                                                 | 194 us: 1.19x slower                                   |
| docutils                 | 1.44 sec                                               | 1.73 sec: 1.20x slower                                 |
| pprint_safe_repr         | 531 ms                                                 | 641 ms: 1.21x slower                                   |
| pprint_pformat           | 1.08 sec                                               | 1.30 sec: 1.21x slower                                 |
| scimark_sor              | 106 ms                                                 | 128 ms: 1.21x slower                                   |
| regex_compile            | 78.5 ms                                                | 95.3 ms: 1.21x slower                                  |
| pyflate                  | 351 ms                                                 | 427 ms: 1.22x slower                                   |
| sympy_sum                | 75.6 ms                                                | 92.2 ms: 1.22x slower                                  |
| float                    | 56.2 ms                                                | 69.0 ms: 1.23x slower                                  |
| spectral_norm            | 77.3 ms                                                | 94.8 ms: 1.23x slower                                  |
| thrift                   | 466 us                                                 | 572 us: 1.23x slower                                   |
| dulwich_log              | 28.7 ms                                                | 35.3 ms: 1.23x slower                                  |
| chameleon                | 5.08 ms                                                | 6.26 ms: 1.23x slower                                  |
| json_dumps               | 6.56 ms                                                | 8.11 ms: 1.24x slower                                  |
| pycparser                | 706 ms                                                 | 877 ms: 1.24x slower                                   |
| logging_simple           | 3.57 us                                                | 4.45 us: 1.24x slower                                  |
| logging_format           | 3.85 us                                                | 4.83 us: 1.25x slower                                  |
| nbody                    | 73.9 ms                                                | 93.0 ms: 1.26x slower                                  |
| asyncio_tcp_ssl          | 1.26 sec                                               | 1.60 sec: 1.27x slower                                 |
| deepcopy_memo            | 27.2 us                                                | 34.7 us: 1.28x slower                                  |
| hexiom                   | 4.85 ms                                                | 6.19 ms: 1.28x slower                                  |
| mako                     | 7.68 ms                                                | 9.87 ms: 1.29x slower                                  |
| scimark_monte_carlo      | 50.4 ms                                                | 65.6 ms: 1.30x slower                                  |
| go                       | 115 ms                                                 | 151 ms: 1.31x slower                                   |
| pickle_pure_python       | 213 us                                                 | 281 us: 1.32x slower                                   |
| crypto_pyaes             | 54.0 ms                                                | 71.8 ms: 1.33x slower                                  |
| scimark_lu               | 76.5 ms                                                | 103 ms: 1.34x slower                                   |
| richards                 | 35.4 ms                                                | 48.7 ms: 1.37x slower                                  |
| comprehensions           | 12.2 us                                                | 16.9 us: 1.39x slower                                  |
| sqlglot_transpile        | 1.02 ms                                                | 1.44 ms: 1.41x slower                                  |
| async_tree_cpu_io_mixed  | 460 ms                                                 | 649 ms: 1.41x slower                                   |
| asyncio_tcp              | 457 ms                                                 | 659 ms: 1.44x slower                                   |
| sqlglot_parse            | 856 us                                                 | 1.24 ms: 1.45x slower                                  |
| richards_super           | 39.1 ms                                                | 57.8 ms: 1.48x slower                                  |
| pylint                   | 181 ms                                                 | 277 ms: 1.53x slower                                   |
| mypy2                    | 396 ms                                                 | 607 ms: 1.53x slower                                   |
| chaos                    | 41.3 ms                                                | 65.8 ms: 1.59x slower                                  |
| raytrace                 | 182 ms                                                 | 301 ms: 1.66x slower                                   |
| logging_silent           | 69.9 ns                                                | 117 ns: 1.68x slower                                   |
| asyncio_websockets       | 241 ms                                                 | 410 ms: 1.70x slower                                   |
| async_tree_memoization   | 270 ms                                                 | 474 ms: 1.75x slower                                   |
| deltablue                | 2.68 ms                                                | 4.91 ms: 1.83x slower                                  |
| async_tree_none          | 212 ms                                                 | 388 ms: 1.83x slower                                   |
| async_tree_io            | 507 ms                                                 | 980 ms: 1.93x slower                                   |
| typing_runtime_protocols | 101 us                                                 | 323 us: 3.20x slower                                   |
| Geometric mean           | (ref)                                                  | 1.16x slower                                           |

Benchmark hidden because not significant (4): aiohttp, gunicorn, dask, tornado_http
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
Ignored benchmarks (2) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.14x
- 95% likely to have a slowdown of 1.13x
- 99% likely to have a slowdown of 1.11x

# Memory
- memory change: 5.17x