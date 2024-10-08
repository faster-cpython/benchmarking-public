# Results vs. 3.10.4

- fork: python
- ref: v3.13.0b2
- machine: darwin-arm64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 1.44x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 173 ms: 1.11x faster                                       |
| chameleon      | 6.26 ms                                                | 4.41 ms: 1.42x faster                                      |
| docutils       | 1.73 sec                                               | 1.51 sec: 1.14x faster                                     |
| html5lib       | 42.4 ms                                                | 31.1 ms: 1.36x faster                                      |
| tornado_http   | 86.7 ms                                                | 68.1 ms: 1.27x faster                                      |
| Geometric mean | (ref)                                                  | 1.26x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 212 ms: 1.83x faster                                       |
| async_tree_memoization  | 474 ms                                                 | 263 ms: 1.80x faster                                       |
| async_tree_io           | 980 ms                                                 | 571 ms: 1.71x faster                                       |
| async_tree_cpu_io_mixed | 649 ms                                                 | 472 ms: 1.38x faster                                       |
| Geometric mean          | (ref)                                                  | 1.67x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 63.5 ms: 1.47x faster                                      |
| float          | 69.0 ms                                                | 47.4 ms: 1.46x faster                                      |
| Geometric mean | (ref)                                                  | 1.29x faster                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 71.9 ms: 1.33x faster                                      |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                       |
| regex_v8       | 17.1 ms                                                | 17.3 ms: 1.01x slower                                      |
| regex_effbot   | 2.46 ms                                                | 2.58 ms: 1.05x slower                                      |
| Geometric mean | (ref)                                                  | 1.10x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 173 us: 1.62x faster                                       |
| unpickle_pure_python | 194 us                                                 | 132 us: 1.47x faster                                       |
| tomli_loads          | 1.71 sec                                               | 1.24 sec: 1.37x faster                                     |
| json_dumps           | 8.11 ms                                                | 6.17 ms: 1.31x faster                                      |
| xml_etree_process    | 46.5 ms                                                | 35.8 ms: 1.30x faster                                      |
| xml_etree_generate   | 53.5 ms                                                | 51.6 ms: 1.04x faster                                      |
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.03x faster                                       |
| xml_etree_iterparse  | 72.1 ms                                                | 70.5 ms: 1.02x faster                                      |
| json_loads           | 16.4 us                                                | 16.9 us: 1.03x slower                                      |
| unpickle             | 8.80 us                                                | 9.19 us: 1.04x slower                                      |
| unpickle_list        | 2.69 us                                                | 2.88 us: 1.07x slower                                      |
| pickle_dict          | 17.0 us                                                | 18.2 us: 1.07x slower                                      |
| pickle               | 6.97 us                                                | 7.52 us: 1.08x slower                                      |
| pickle_list          | 2.74 us                                                | 2.99 us: 1.09x slower                                      |
| Geometric mean       | (ref)                                                  | 1.11x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 16.4 ms: 1.50x slower                                      |
| python_startup_no_site | 7.91 ms                                                | 13.4 ms: 1.70x slower                                      |
| Geometric mean         | (ref)                                                  | 1.60x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.40 ms: 1.54x faster                                      |
| django_template | 26.4 ms                                                | 21.3 ms: 1.24x faster                                      |
| genshi_text     | 17.3 ms                                                | 16.4 ms: 1.06x faster                                      |
| genshi_xml      | 33.8 ms                                                | 39.3 ms: 1.16x slower                                      |
| Geometric mean  | (ref)                                                  | 1.15x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 93.5 us: 3.46x faster                                      |
| deltablue                | 4.91 ms                                                | 2.47 ms: 1.99x faster                                      |
| logging_silent           | 117 ns                                                 | 63.1 ns: 1.86x faster                                      |
| raytrace                 | 301 ms                                                 | 163 ms: 1.85x faster                                       |
| async_tree_none          | 388 ms                                                 | 212 ms: 1.83x faster                                       |
| async_tree_memoization   | 474 ms                                                 | 263 ms: 1.80x faster                                       |
| async_tree_io            | 980 ms                                                 | 571 ms: 1.71x faster                                       |
| chaos                    | 65.8 ms                                                | 38.9 ms: 1.69x faster                                      |
| richards_super           | 57.8 ms                                                | 35.7 ms: 1.62x faster                                      |
| pickle_pure_python       | 281 us                                                 | 173 us: 1.62x faster                                       |
| deepcopy_memo            | 34.7 us                                                | 21.5 us: 1.62x faster                                      |
| asyncio_tcp              | 659 ms                                                 | 417 ms: 1.58x faster                                       |
| mako                     | 9.87 ms                                                | 6.40 ms: 1.54x faster                                      |
| richards                 | 48.7 ms                                                | 31.7 ms: 1.53x faster                                      |
| pylint                   | 277 ms                                                 | 183 ms: 1.51x faster                                       |
| sqlglot_parse            | 1.24 ms                                                | 826 us: 1.51x faster                                       |
| scimark_monte_carlo      | 65.6 ms                                                | 44.0 ms: 1.49x faster                                      |
| mypy2                    | 607 ms                                                 | 408 ms: 1.49x faster                                       |
| go                       | 151 ms                                                 | 102 ms: 1.48x faster                                       |
| unpickle_pure_python     | 194 us                                                 | 132 us: 1.47x faster                                       |
| logging_simple           | 4.45 us                                                | 3.02 us: 1.47x faster                                      |
| nbody                    | 93.0 ms                                                | 63.5 ms: 1.47x faster                                      |
| float                    | 69.0 ms                                                | 47.4 ms: 1.46x faster                                      |
| logging_format           | 4.83 us                                                | 3.33 us: 1.45x faster                                      |
| sqlglot_transpile        | 1.44 ms                                                | 1.00 ms: 1.44x faster                                      |
| hexiom                   | 6.19 ms                                                | 4.36 ms: 1.42x faster                                      |
| chameleon                | 6.26 ms                                                | 4.41 ms: 1.42x faster                                      |
| spectral_norm            | 94.8 ms                                                | 67.5 ms: 1.40x faster                                      |
| crypto_pyaes             | 71.8 ms                                                | 51.8 ms: 1.39x faster                                      |
| comprehensions           | 16.9 us                                                | 12.2 us: 1.38x faster                                      |
| pprint_safe_repr         | 641 ms                                                 | 464 ms: 1.38x faster                                       |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 472 ms: 1.38x faster                                       |
| tomli_loads              | 1.71 sec                                               | 1.24 sec: 1.37x faster                                     |
| generators               | 32.3 ms                                                | 23.6 ms: 1.37x faster                                      |
| pprint_pformat           | 1.30 sec                                               | 958 ms: 1.36x faster                                       |
| html5lib                 | 42.4 ms                                                | 31.1 ms: 1.36x faster                                      |
| pyflate                  | 427 ms                                                 | 315 ms: 1.35x faster                                       |
| regex_compile            | 95.3 ms                                                | 71.9 ms: 1.33x faster                                      |
| json_dumps               | 8.11 ms                                                | 6.17 ms: 1.31x faster                                      |
| scimark_lu               | 103 ms                                                 | 78.6 ms: 1.31x faster                                      |
| deepcopy                 | 272 us                                                 | 208 us: 1.31x faster                                       |
| thrift                   | 572 us                                                 | 438 us: 1.31x faster                                       |
| pycparser                | 877 ms                                                 | 672 ms: 1.30x faster                                       |
| fannkuch                 | 303 ms                                                 | 233 ms: 1.30x faster                                       |
| xml_etree_process        | 46.5 ms                                                | 35.8 ms: 1.30x faster                                      |
| coroutines               | 20.7 ms                                                | 16.0 ms: 1.29x faster                                      |
| deepcopy_reduce          | 2.33 us                                                | 1.82 us: 1.28x faster                                      |
| scimark_sor              | 128 ms                                                 | 100 ms: 1.28x faster                                       |
| tornado_http             | 86.7 ms                                                | 68.1 ms: 1.27x faster                                      |
| sympy_sum                | 92.2 ms                                                | 72.4 ms: 1.27x faster                                      |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.30 sec: 1.24x faster                                     |
| django_template          | 26.4 ms                                                | 21.3 ms: 1.24x faster                                      |
| dulwich_log              | 35.3 ms                                                | 28.8 ms: 1.23x faster                                      |
| scimark_fft              | 224 ms                                                 | 185 ms: 1.21x faster                                       |
| sympy_str                | 165 ms                                                 | 137 ms: 1.21x faster                                       |
| sympy_integrate          | 13.1 ms                                                | 10.9 ms: 1.21x faster                                      |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.92 ms: 1.17x faster                                      |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                       |
| docutils                 | 1.73 sec                                               | 1.51 sec: 1.14x faster                                     |
| mdp                      | 1.63 sec                                               | 1.43 sec: 1.14x faster                                     |
| sympy_expand             | 269 ms                                                 | 236 ms: 1.14x faster                                       |
| gunicorn                 | 1.30 ms                                                | 1.15 ms: 1.13x faster                                      |
| dask                     | 253 ms                                                 | 223 ms: 1.13x faster                                       |
| sqlglot_optimize         | 36.8 ms                                                | 32.6 ms: 1.13x faster                                      |
| nqueens                  | 63.8 ms                                                | 56.8 ms: 1.12x faster                                      |
| aiohttp                  | 1.22 ms                                                | 1.10 ms: 1.11x faster                                      |
| 2to3                     | 192 ms                                                 | 173 ms: 1.11x faster                                       |
| bench_thread_pool        | 527 us                                                 | 481 us: 1.10x faster                                       |
| meteor_contest           | 77.7 ms                                                | 71.4 ms: 1.09x faster                                      |
| genshi_text              | 17.3 ms                                                | 16.4 ms: 1.06x faster                                      |
| json                     | 3.08 ms                                                | 2.93 ms: 1.05x faster                                      |
| pathlib                  | 24.5 ms                                                | 23.4 ms: 1.05x faster                                      |
| xml_etree_generate       | 53.5 ms                                                | 51.6 ms: 1.04x faster                                      |
| xml_etree_parse          | 108 ms                                                 | 105 ms: 1.03x faster                                       |
| xml_etree_iterparse      | 72.1 ms                                                | 70.5 ms: 1.02x faster                                      |
| regex_v8                 | 17.1 ms                                                | 17.3 ms: 1.01x slower                                      |
| json_loads               | 16.4 us                                                | 16.9 us: 1.03x slower                                      |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                      |
| unpickle                 | 8.80 us                                                | 9.19 us: 1.04x slower                                      |
| regex_effbot             | 2.46 ms                                                | 2.58 ms: 1.05x slower                                      |
| create_gc_cycles         | 860 us                                                 | 903 us: 1.05x slower                                       |
| unpickle_list            | 2.69 us                                                | 2.88 us: 1.07x slower                                      |
| pickle_dict              | 17.0 us                                                | 18.2 us: 1.07x slower                                      |
| sqlite_synth             | 1.46 us                                                | 1.57 us: 1.07x slower                                      |
| pickle                   | 6.97 us                                                | 7.52 us: 1.08x slower                                      |
| coverage                 | 41.5 ms                                                | 44.9 ms: 1.08x slower                                      |
| pickle_list              | 2.74 us                                                | 2.99 us: 1.09x slower                                      |
| genshi_xml               | 33.8 ms                                                | 39.3 ms: 1.16x slower                                      |
| async_generators         | 231 ms                                                 | 296 ms: 1.28x slower                                       |
| telco                    | 3.49 ms                                                | 4.64 ms: 1.33x slower                                      |
| flaskblogging            | 2.65 ms                                                | 3.61 ms: 1.36x slower                                      |
| bench_mp_pool            | 37.4 ms                                                | 51.4 ms: 1.37x slower                                      |
| python_startup           | 10.9 ms                                                | 16.4 ms: 1.50x slower                                      |
| python_startup_no_site   | 7.91 ms                                                | 13.4 ms: 1.70x slower                                      |
| Geometric mean           | (ref)                                                  | 1.23x faster                                               |

Benchmark hidden because not significant (2): asyncio_websockets, pidigits
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 1.44x