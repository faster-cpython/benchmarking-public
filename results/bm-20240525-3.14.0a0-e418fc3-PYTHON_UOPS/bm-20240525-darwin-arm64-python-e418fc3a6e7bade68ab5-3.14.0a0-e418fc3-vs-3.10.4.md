# Results vs. 3.10.4

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: darwin-arm64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.10x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 0.79x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 182 ms: 1.05x faster                                                  |
| chameleon      | 6.26 ms                                                | 4.99 ms: 1.25x faster                                                 |
| docutils       | 1.73 sec                                               | 1.68 sec: 1.03x faster                                                |
| html5lib       | 42.4 ms                                                | 33.3 ms: 1.27x faster                                                 |
| tornado_http   | 86.7 ms                                                | 70.6 ms: 1.23x faster                                                 |
| Geometric mean | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 226 ms: 1.71x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 279 ms: 1.70x faster                                                  |
| async_tree_io           | 980 ms                                                 | 587 ms: 1.67x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 488 ms: 1.33x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.59x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 76.1 ms: 1.22x faster                                                 |
| float          | 69.0 ms                                                | 61.3 ms: 1.12x faster                                                 |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                                  |
| regex_compile  | 95.3 ms                                                | 96.5 ms: 1.01x slower                                                 |
| regex_v8       | 17.1 ms                                                | 17.6 ms: 1.03x slower                                                 |
| regex_effbot   | 2.46 ms                                                | 2.59 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 228 us: 1.23x faster                                                  |
| json_dumps           | 8.11 ms                                                | 6.62 ms: 1.22x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 41.4 ms: 1.12x faster                                                 |
| unpickle_pure_python | 194 us                                                 | 179 us: 1.09x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.65 sec: 1.03x faster                                                |
| xml_etree_parse      | 108 ms                                                 | 106 ms: 1.01x faster                                                  |
| json_loads           | 16.4 us                                                | 17.0 us: 1.03x slower                                                 |
| unpickle             | 8.80 us                                                | 9.28 us: 1.05x slower                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 76.6 ms: 1.06x slower                                                 |
| pickle               | 6.97 us                                                | 7.41 us: 1.06x slower                                                 |
| pickle_dict          | 17.0 us                                                | 18.2 us: 1.07x slower                                                 |
| unpickle_list        | 2.69 us                                                | 2.90 us: 1.08x slower                                                 |
| pickle_list          | 2.74 us                                                | 2.95 us: 1.08x slower                                                 |
| xml_etree_generate   | 53.5 ms                                                | 59.0 ms: 1.10x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 14.6 ms: 1.35x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 12.0 ms: 1.52x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.43x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 26.4 ms                                                | 24.1 ms: 1.10x faster                                                 |
| mako            | 9.87 ms                                                | 9.12 ms: 1.08x faster                                                 |
| genshi_text     | 17.3 ms                                                | 17.5 ms: 1.01x slower                                                 |
| genshi_xml      | 33.8 ms                                                | 36.4 ms: 1.08x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 109 us: 2.96x faster                                                  |
| async_tree_none          | 388 ms                                                 | 226 ms: 1.71x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 279 ms: 1.70x faster                                                  |
| raytrace                 | 301 ms                                                 | 178 ms: 1.69x faster                                                  |
| deltablue                | 4.91 ms                                                | 2.93 ms: 1.68x faster                                                 |
| async_tree_io            | 980 ms                                                 | 587 ms: 1.67x faster                                                  |
| asyncio_tcp              | 659 ms                                                 | 406 ms: 1.62x faster                                                  |
| pylint                   | 277 ms                                                 | 194 ms: 1.43x faster                                                  |
| richards_super           | 57.8 ms                                                | 40.9 ms: 1.41x faster                                                 |
| chaos                    | 65.8 ms                                                | 46.8 ms: 1.41x faster                                                 |
| generators               | 32.3 ms                                                | 23.4 ms: 1.38x faster                                                 |
| logging_simple           | 4.45 us                                                | 3.25 us: 1.37x faster                                                 |
| logging_format           | 4.83 us                                                | 3.56 us: 1.36x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 488 ms: 1.33x faster                                                  |
| richards                 | 48.7 ms                                                | 37.3 ms: 1.31x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 958 us: 1.30x faster                                                  |
| thrift                   | 572 us                                                 | 443 us: 1.29x faster                                                  |
| go                       | 151 ms                                                 | 117 ms: 1.29x faster                                                  |
| html5lib                 | 42.4 ms                                                | 33.3 ms: 1.27x faster                                                 |
| chameleon                | 6.26 ms                                                | 4.99 ms: 1.25x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.6 ms: 1.25x faster                                                 |
| sqlglot_transpile        | 1.44 ms                                                | 1.16 ms: 1.25x faster                                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.29 sec: 1.24x faster                                                |
| pickle_pure_python       | 281 us                                                 | 228 us: 1.23x faster                                                  |
| tornado_http             | 86.7 ms                                                | 70.6 ms: 1.23x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.62 ms: 1.22x faster                                                 |
| logging_silent           | 117 ns                                                 | 95.9 ns: 1.22x faster                                                 |
| nbody                    | 93.0 ms                                                | 76.1 ms: 1.22x faster                                                 |
| scimark_sor              | 128 ms                                                 | 107 ms: 1.20x faster                                                  |
| pycparser                | 877 ms                                                 | 731 ms: 1.20x faster                                                  |
| crypto_pyaes             | 71.8 ms                                                | 61.3 ms: 1.17x faster                                                 |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                                  |
| float                    | 69.0 ms                                                | 61.3 ms: 1.12x faster                                                 |
| xml_etree_process        | 46.5 ms                                                | 41.4 ms: 1.12x faster                                                 |
| pprint_safe_repr         | 641 ms                                                 | 576 ms: 1.11x faster                                                  |
| dask                     | 253 ms                                                 | 228 ms: 1.11x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 1.18 sec: 1.11x faster                                                |
| django_template          | 26.4 ms                                                | 24.1 ms: 1.10x faster                                                 |
| unpickle_pure_python     | 194 us                                                 | 179 us: 1.09x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 2.15 us: 1.08x faster                                                 |
| mako                     | 9.87 ms                                                | 9.12 ms: 1.08x faster                                                 |
| deepcopy                 | 272 us                                                 | 253 us: 1.08x faster                                                  |
| pyflate                  | 427 ms                                                 | 399 ms: 1.07x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 61.4 ms: 1.07x faster                                                 |
| pathlib                  | 24.5 ms                                                | 23.0 ms: 1.07x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 32.6 us: 1.06x faster                                                 |
| sympy_sum                | 92.2 ms                                                | 87.2 ms: 1.06x faster                                                 |
| 2to3                     | 192 ms                                                 | 182 ms: 1.05x faster                                                  |
| json                     | 3.08 ms                                                | 2.98 ms: 1.04x faster                                                 |
| hexiom                   | 6.19 ms                                                | 5.98 ms: 1.04x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 12.7 ms: 1.03x faster                                                 |
| docutils                 | 1.73 sec                                               | 1.68 sec: 1.03x faster                                                |
| tomli_loads              | 1.71 sec                                               | 1.65 sec: 1.03x faster                                                |
| scimark_lu               | 103 ms                                                 | 100.0 ms: 1.03x faster                                                |
| xml_etree_parse          | 108 ms                                                 | 106 ms: 1.01x faster                                                  |
| sympy_expand             | 269 ms                                                 | 266 ms: 1.01x faster                                                  |
| scimark_fft              | 224 ms                                                 | 223 ms: 1.01x faster                                                  |
| spectral_norm            | 94.8 ms                                                | 94.6 ms: 1.00x faster                                                 |
| genshi_text              | 17.3 ms                                                | 17.5 ms: 1.01x slower                                                 |
| bench_thread_pool        | 527 us                                                 | 533 us: 1.01x slower                                                  |
| mdp                      | 1.63 sec                                               | 1.65 sec: 1.01x slower                                                |
| regex_compile            | 95.3 ms                                                | 96.5 ms: 1.01x slower                                                 |
| sqlglot_optimize         | 36.8 ms                                                | 37.6 ms: 1.02x slower                                                 |
| regex_v8                 | 17.1 ms                                                | 17.6 ms: 1.03x slower                                                 |
| meteor_contest           | 77.7 ms                                                | 80.1 ms: 1.03x slower                                                 |
| json_loads               | 16.4 us                                                | 17.0 us: 1.03x slower                                                 |
| comprehensions           | 16.9 us                                                | 17.5 us: 1.03x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.47 ms: 1.05x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 905 us: 1.05x slower                                                  |
| regex_effbot             | 2.46 ms                                                | 2.59 ms: 1.05x slower                                                 |
| fannkuch                 | 303 ms                                                 | 319 ms: 1.05x slower                                                  |
| unpickle                 | 8.80 us                                                | 9.28 us: 1.05x slower                                                 |
| xml_etree_iterparse      | 72.1 ms                                                | 76.6 ms: 1.06x slower                                                 |
| pickle                   | 6.97 us                                                | 7.41 us: 1.06x slower                                                 |
| pickle_dict              | 17.0 us                                                | 18.2 us: 1.07x slower                                                 |
| unpickle_list            | 2.69 us                                                | 2.90 us: 1.08x slower                                                 |
| genshi_xml               | 33.8 ms                                                | 36.4 ms: 1.08x slower                                                 |
| pickle_list              | 2.74 us                                                | 2.95 us: 1.08x slower                                                 |
| nqueens                  | 63.8 ms                                                | 69.1 ms: 1.08x slower                                                 |
| xml_etree_generate       | 53.5 ms                                                | 59.0 ms: 1.10x slower                                                 |
| sqlite_synth             | 1.46 us                                                | 1.61 us: 1.10x slower                                                 |
| coverage                 | 41.5 ms                                                | 46.2 ms: 1.11x slower                                                 |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.82 ms: 1.12x slower                                                 |
| bench_mp_pool            | 37.4 ms                                                | 47.5 ms: 1.27x slower                                                 |
| async_generators         | 231 ms                                                 | 295 ms: 1.28x slower                                                  |
| flaskblogging            | 2.65 ms                                                | 3.56 ms: 1.34x slower                                                 |
| python_startup           | 10.9 ms                                                | 14.6 ms: 1.35x slower                                                 |
| telco                    | 3.49 ms                                                | 5.05 ms: 1.45x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 12.0 ms: 1.52x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (3): asyncio_websockets, pidigits, sympy_str
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (12) of results/bm-20240525-3.14.0a0-e418fc3-PYTHON_UOPS/bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 0.79x