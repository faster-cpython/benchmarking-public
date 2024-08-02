# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a3
- machine: darwin-arm64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.17x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 170 ms: 1.12x faster                                       |
| chameleon      | 6.26 ms                                                | 4.87 ms: 1.29x faster                                      |
| docutils       | 1.73 sec                                               | 1.46 sec: 1.19x faster                                     |
| html5lib       | 42.4 ms                                                | 35.9 ms: 1.18x faster                                      |
| tornado_http   | 86.7 ms                                                | 78.1 ms: 1.11x faster                                      |
| Geometric mean | (ref)                                                  | 1.18x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 253 ms: 1.53x faster                                       |
| async_tree_memoization  | 474 ms                                                 | 329 ms: 1.44x faster                                       |
| async_tree_io           | 980 ms                                                 | 703 ms: 1.39x faster                                       |
| async_tree_cpu_io_mixed | 649 ms                                                 | 521 ms: 1.25x faster                                       |
| Geometric mean          | (ref)                                                  | 1.40x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 75.6 ms: 1.23x faster                                      |
| float          | 69.0 ms                                                | 56.9 ms: 1.21x faster                                      |
| Geometric mean | (ref)                                                  | 1.14x faster                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 73.8 ms: 1.29x faster                                      |
| regex_dna      | 174 ms                                                 | 157 ms: 1.11x faster                                       |
| regex_v8       | 17.1 ms                                                | 18.0 ms: 1.05x slower                                      |
| regex_effbot   | 2.46 ms                                                | 2.77 ms: 1.13x slower                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 198 us: 1.42x faster                                       |
| unpickle_pure_python | 194 us                                                 | 154 us: 1.26x faster                                       |
| json_dumps           | 8.11 ms                                                | 6.52 ms: 1.24x faster                                      |
| xml_etree_process    | 46.5 ms                                                | 39.9 ms: 1.17x faster                                      |
| tomli_loads          | 1.71 sec                                               | 1.54 sec: 1.10x faster                                     |
| xml_etree_parse      | 108 ms                                                 | 99.6 ms: 1.08x faster                                      |
| xml_etree_iterparse  | 72.1 ms                                                | 71.9 ms: 1.00x faster                                      |
| json_loads           | 16.4 us                                                | 17.1 us: 1.04x slower                                      |
| xml_etree_generate   | 53.5 ms                                                | 56.3 ms: 1.05x slower                                      |
| unpickle             | 8.80 us                                                | 9.29 us: 1.06x slower                                      |
| pickle               | 6.97 us                                                | 7.41 us: 1.06x slower                                      |
| pickle_list          | 2.74 us                                                | 2.93 us: 1.07x slower                                      |
| pickle_dict          | 17.0 us                                                | 18.2 us: 1.07x slower                                      |
| unpickle_list        | 2.69 us                                                | 3.11 us: 1.15x slower                                      |
| Geometric mean       | (ref)                                                  | 1.05x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 13.9 ms: 1.28x slower                                      |
| python_startup_no_site | 7.91 ms                                                | 12.3 ms: 1.56x slower                                      |
| Geometric mean         | (ref)                                                  | 1.41x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.54 ms: 1.31x faster                                      |
| django_template | 26.4 ms                                                | 21.7 ms: 1.22x faster                                      |
| genshi_text     | 17.3 ms                                                | 15.8 ms: 1.10x faster                                      |
| genshi_xml      | 33.8 ms                                                | 33.6 ms: 1.01x faster                                      |
| Geometric mean  | (ref)                                                  | 1.15x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 70.9 us: 4.56x faster                                      |
| deltablue                | 4.91 ms                                                | 2.44 ms: 2.01x faster                                      |
| raytrace                 | 301 ms                                                 | 171 ms: 1.76x faster                                       |
| logging_silent           | 117 ns                                                 | 69.9 ns: 1.68x faster                                      |
| chaos                    | 65.8 ms                                                | 39.8 ms: 1.65x faster                                      |
| pylint                   | 277 ms                                                 | 169 ms: 1.64x faster                                       |
| asyncio_tcp              | 659 ms                                                 | 404 ms: 1.63x faster                                       |
| sqlglot_parse            | 1.24 ms                                                | 789 us: 1.58x faster                                       |
| richards_super           | 57.8 ms                                                | 37.3 ms: 1.55x faster                                      |
| async_tree_none          | 388 ms                                                 | 253 ms: 1.53x faster                                       |
| sqlglot_transpile        | 1.44 ms                                                | 965 us: 1.49x faster                                       |
| crypto_pyaes             | 71.8 ms                                                | 48.3 ms: 1.49x faster                                      |
| richards                 | 48.7 ms                                                | 33.8 ms: 1.44x faster                                      |
| async_tree_memoization   | 474 ms                                                 | 329 ms: 1.44x faster                                       |
| go                       | 151 ms                                                 | 106 ms: 1.43x faster                                       |
| pickle_pure_python       | 281 us                                                 | 198 us: 1.42x faster                                       |
| comprehensions           | 16.9 us                                                | 12.1 us: 1.40x faster                                      |
| async_tree_io            | 980 ms                                                 | 703 ms: 1.39x faster                                       |
| scimark_lu               | 103 ms                                                 | 74.2 ms: 1.39x faster                                      |
| scimark_monte_carlo      | 65.6 ms                                                | 47.5 ms: 1.38x faster                                      |
| hexiom                   | 6.19 ms                                                | 4.57 ms: 1.35x faster                                      |
| deepcopy_memo            | 34.7 us                                                | 25.7 us: 1.35x faster                                      |
| mako                     | 9.87 ms                                                | 7.54 ms: 1.31x faster                                      |
| regex_compile            | 95.3 ms                                                | 73.8 ms: 1.29x faster                                      |
| chameleon                | 6.26 ms                                                | 4.87 ms: 1.29x faster                                      |
| logging_simple           | 4.45 us                                                | 3.49 us: 1.28x faster                                      |
| logging_format           | 4.83 us                                                | 3.79 us: 1.27x faster                                      |
| sympy_sum                | 92.2 ms                                                | 72.5 ms: 1.27x faster                                      |
| unpickle_pure_python     | 194 us                                                 | 154 us: 1.26x faster                                       |
| pyflate                  | 427 ms                                                 | 339 ms: 1.26x faster                                       |
| spectral_norm            | 94.8 ms                                                | 75.4 ms: 1.26x faster                                      |
| pycparser                | 877 ms                                                 | 700 ms: 1.25x faster                                       |
| thrift                   | 572 us                                                 | 458 us: 1.25x faster                                       |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 521 ms: 1.25x faster                                       |
| json_dumps               | 8.11 ms                                                | 6.52 ms: 1.24x faster                                      |
| pprint_pformat           | 1.30 sec                                               | 1.05 sec: 1.24x faster                                     |
| pprint_safe_repr         | 641 ms                                                 | 516 ms: 1.24x faster                                       |
| nbody                    | 93.0 ms                                                | 75.6 ms: 1.23x faster                                      |
| sympy_integrate          | 13.1 ms                                                | 10.7 ms: 1.22x faster                                      |
| scimark_sor              | 128 ms                                                 | 105 ms: 1.22x faster                                       |
| create_gc_cycles         | 860 us                                                 | 706 us: 1.22x faster                                       |
| django_template          | 26.4 ms                                                | 21.7 ms: 1.22x faster                                      |
| float                    | 69.0 ms                                                | 56.9 ms: 1.21x faster                                      |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.32 sec: 1.21x faster                                     |
| deepcopy                 | 272 us                                                 | 225 us: 1.21x faster                                       |
| dulwich_log              | 35.3 ms                                                | 29.4 ms: 1.20x faster                                      |
| docutils                 | 1.73 sec                                               | 1.46 sec: 1.19x faster                                     |
| sympy_str                | 165 ms                                                 | 140 ms: 1.18x faster                                       |
| html5lib                 | 42.4 ms                                                | 35.9 ms: 1.18x faster                                      |
| deepcopy_reduce          | 2.33 us                                                | 1.98 us: 1.18x faster                                      |
| xml_etree_process        | 46.5 ms                                                | 39.9 ms: 1.17x faster                                      |
| generators               | 32.3 ms                                                | 28.4 ms: 1.14x faster                                      |
| sympy_expand             | 269 ms                                                 | 238 ms: 1.13x faster                                       |
| 2to3                     | 192 ms                                                 | 170 ms: 1.12x faster                                       |
| regex_dna                | 174 ms                                                 | 157 ms: 1.11x faster                                       |
| tornado_http             | 86.7 ms                                                | 78.1 ms: 1.11x faster                                      |
| fannkuch                 | 303 ms                                                 | 273 ms: 1.11x faster                                       |
| coroutines               | 20.7 ms                                                | 18.7 ms: 1.11x faster                                      |
| tomli_loads              | 1.71 sec                                               | 1.54 sec: 1.10x faster                                     |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.11 ms: 1.10x faster                                      |
| genshi_text              | 17.3 ms                                                | 15.8 ms: 1.10x faster                                      |
| scimark_fft              | 224 ms                                                 | 204 ms: 1.10x faster                                       |
| sqlglot_optimize         | 36.8 ms                                                | 33.9 ms: 1.08x faster                                      |
| xml_etree_parse          | 108 ms                                                 | 99.6 ms: 1.08x faster                                      |
| meteor_contest           | 77.7 ms                                                | 72.7 ms: 1.07x faster                                      |
| bench_thread_pool        | 527 us                                                 | 500 us: 1.06x faster                                       |
| nqueens                  | 63.8 ms                                                | 60.9 ms: 1.05x faster                                      |
| mdp                      | 1.63 sec                                               | 1.56 sec: 1.04x faster                                     |
| sqlglot_normalize        | 190 ms                                                 | 183 ms: 1.04x faster                                       |
| json                     | 3.08 ms                                                | 2.98 ms: 1.04x faster                                      |
| genshi_xml               | 33.8 ms                                                | 33.6 ms: 1.01x faster                                      |
| xml_etree_iterparse      | 72.1 ms                                                | 71.9 ms: 1.00x faster                                      |
| gc_traversal             | 2.36 ms                                                | 2.40 ms: 1.02x slower                                      |
| json_loads               | 16.4 us                                                | 17.1 us: 1.04x slower                                      |
| regex_v8                 | 17.1 ms                                                | 18.0 ms: 1.05x slower                                      |
| xml_etree_generate       | 53.5 ms                                                | 56.3 ms: 1.05x slower                                      |
| unpickle                 | 8.80 us                                                | 9.29 us: 1.06x slower                                      |
| pickle                   | 6.97 us                                                | 7.41 us: 1.06x slower                                      |
| pickle_list              | 2.74 us                                                | 2.93 us: 1.07x slower                                      |
| pickle_dict              | 17.0 us                                                | 18.2 us: 1.07x slower                                      |
| sqlite_synth             | 1.46 us                                                | 1.60 us: 1.10x slower                                      |
| regex_effbot             | 2.46 ms                                                | 2.77 ms: 1.13x slower                                      |
| coverage                 | 41.5 ms                                                | 47.2 ms: 1.14x slower                                      |
| unpickle_list            | 2.69 us                                                | 3.11 us: 1.15x slower                                      |
| bench_mp_pool            | 37.4 ms                                                | 45.1 ms: 1.21x slower                                      |
| async_generators         | 231 ms                                                 | 296 ms: 1.28x slower                                       |
| python_startup           | 10.9 ms                                                | 13.9 ms: 1.28x slower                                      |
| telco                    | 3.49 ms                                                | 4.65 ms: 1.33x slower                                      |
| flaskblogging            | 2.65 ms                                                | 3.94 ms: 1.49x slower                                      |
| python_startup_no_site   | 7.91 ms                                                | 12.3 ms: 1.56x slower                                      |
| Geometric mean           | (ref)                                                  | 1.17x faster                                               |

Benchmark hidden because not significant (6): mypy2, gunicorn, asyncio_websockets, pathlib, pidigits, aiohttp
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (12) of results/bm-20240117-3.13.0a3-f009305/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: 1.12x