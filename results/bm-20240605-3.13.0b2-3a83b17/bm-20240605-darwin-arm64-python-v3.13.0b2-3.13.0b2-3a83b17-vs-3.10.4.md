# Results vs. 3.10.4

- fork: python
- ref: v3.13.0b2
- machine: darwin-arm64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.27x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 161 ms: 1.19x faster                                       |
| chameleon      | 6.26 ms                                                | 4.27 ms: 1.47x faster                                      |
| docutils       | 1.73 sec                                               | 1.44 sec: 1.21x faster                                     |
| html5lib       | 42.4 ms                                                | 31.2 ms: 1.36x faster                                      |
| tornado_http   | 86.7 ms                                                | 66.7 ms: 1.30x faster                                      |
| Geometric mean | (ref)                                                  | 1.30x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 209 ms: 1.85x faster                                       |
| async_tree_memoization  | 474 ms                                                 | 260 ms: 1.82x faster                                       |
| async_tree_io           | 980 ms                                                 | 563 ms: 1.74x faster                                       |
| async_tree_cpu_io_mixed | 649 ms                                                 | 467 ms: 1.39x faster                                       |
| Geometric mean          | (ref)                                                  | 1.69x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 59.6 ms: 1.56x faster                                      |
| float          | 69.0 ms                                                | 48.6 ms: 1.42x faster                                      |
| Geometric mean | (ref)                                                  | 1.30x faster                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 68.5 ms: 1.39x faster                                      |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                       |
| regex_v8       | 17.1 ms                                                | 17.3 ms: 1.01x slower                                      |
| regex_effbot   | 2.46 ms                                                | 2.58 ms: 1.05x slower                                      |
| Geometric mean | (ref)                                                  | 1.11x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 179 us: 1.57x faster                                       |
| unpickle_pure_python | 194 us                                                 | 141 us: 1.38x faster                                       |
| json_dumps           | 8.11 ms                                                | 6.23 ms: 1.30x faster                                      |
| xml_etree_process    | 46.5 ms                                                | 37.1 ms: 1.26x faster                                      |
| tomli_loads          | 1.71 sec                                               | 1.47 sec: 1.16x faster                                     |
| xml_etree_parse      | 108 ms                                                 | 106 ms: 1.02x faster                                       |
| xml_etree_generate   | 53.5 ms                                                | 52.7 ms: 1.02x faster                                      |
| xml_etree_iterparse  | 72.1 ms                                                | 71.5 ms: 1.01x faster                                      |
| json_loads           | 16.4 us                                                | 16.8 us: 1.02x slower                                      |
| unpickle             | 8.80 us                                                | 9.12 us: 1.04x slower                                      |
| unpickle_list        | 2.69 us                                                | 2.88 us: 1.07x slower                                      |
| pickle               | 6.97 us                                                | 7.48 us: 1.07x slower                                      |
| pickle_dict          | 17.0 us                                                | 18.3 us: 1.08x slower                                      |
| pickle_list          | 2.74 us                                                | 2.96 us: 1.08x slower                                      |
| Geometric mean       | (ref)                                                  | 1.08x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 15.2 ms: 1.39x slower                                      |
| python_startup_no_site | 7.91 ms                                                | 12.3 ms: 1.56x slower                                      |
| Geometric mean         | (ref)                                                  | 1.47x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.99 ms: 1.41x faster                                      |
| django_template | 26.4 ms                                                | 19.4 ms: 1.36x faster                                      |
| genshi_text     | 17.3 ms                                                | 13.9 ms: 1.25x faster                                      |
| genshi_xml      | 33.8 ms                                                | 29.9 ms: 1.13x faster                                      |
| Geometric mean  | (ref)                                                  | 1.28x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 87.6 us: 3.69x faster                                      |
| deltablue                | 4.91 ms                                                | 2.14 ms: 2.30x faster                                      |
| raytrace                 | 301 ms                                                 | 147 ms: 2.05x faster                                       |
| logging_silent           | 117 ns                                                 | 60.1 ns: 1.95x faster                                      |
| chaos                    | 65.8 ms                                                | 34.0 ms: 1.93x faster                                      |
| async_tree_none          | 388 ms                                                 | 209 ms: 1.85x faster                                       |
| async_tree_memoization   | 474 ms                                                 | 260 ms: 1.82x faster                                       |
| async_tree_io            | 980 ms                                                 | 563 ms: 1.74x faster                                       |
| sqlglot_parse            | 1.24 ms                                                | 732 us: 1.70x faster                                       |
| comprehensions           | 16.9 us                                                | 10.2 us: 1.67x faster                                      |
| richards_super           | 57.8 ms                                                | 35.2 ms: 1.64x faster                                      |
| asyncio_tcp              | 659 ms                                                 | 402 ms: 1.64x faster                                       |
| pylint                   | 277 ms                                                 | 170 ms: 1.63x faster                                       |
| sqlglot_transpile        | 1.44 ms                                                | 891 us: 1.62x faster                                       |
| mypy2                    | 607 ms                                                 | 379 ms: 1.60x faster                                       |
| pickle_pure_python       | 281 us                                                 | 179 us: 1.57x faster                                       |
| nbody                    | 93.0 ms                                                | 59.6 ms: 1.56x faster                                      |
| scimark_monte_carlo      | 65.6 ms                                                | 42.5 ms: 1.54x faster                                      |
| scimark_lu               | 103 ms                                                 | 66.9 ms: 1.54x faster                                      |
| deepcopy_memo            | 34.7 us                                                | 22.6 us: 1.54x faster                                      |
| richards                 | 48.7 ms                                                | 31.8 ms: 1.53x faster                                      |
| hexiom                   | 6.19 ms                                                | 4.06 ms: 1.53x faster                                      |
| go                       | 151 ms                                                 | 101 ms: 1.50x faster                                       |
| chameleon                | 6.26 ms                                                | 4.27 ms: 1.47x faster                                      |
| logging_simple           | 4.45 us                                                | 3.04 us: 1.46x faster                                      |
| logging_format           | 4.83 us                                                | 3.31 us: 1.46x faster                                      |
| crypto_pyaes             | 71.8 ms                                                | 49.5 ms: 1.45x faster                                      |
| spectral_norm            | 94.8 ms                                                | 66.4 ms: 1.43x faster                                      |
| float                    | 69.0 ms                                                | 48.6 ms: 1.42x faster                                      |
| mako                     | 9.87 ms                                                | 6.99 ms: 1.41x faster                                      |
| generators               | 32.3 ms                                                | 22.9 ms: 1.41x faster                                      |
| regex_compile            | 95.3 ms                                                | 68.5 ms: 1.39x faster                                      |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 467 ms: 1.39x faster                                       |
| pycparser                | 877 ms                                                 | 632 ms: 1.39x faster                                       |
| unpickle_pure_python     | 194 us                                                 | 141 us: 1.38x faster                                       |
| pprint_safe_repr         | 641 ms                                                 | 465 ms: 1.38x faster                                       |
| pprint_pformat           | 1.30 sec                                               | 947 ms: 1.38x faster                                       |
| django_template          | 26.4 ms                                                | 19.4 ms: 1.36x faster                                      |
| html5lib                 | 42.4 ms                                                | 31.2 ms: 1.36x faster                                      |
| scimark_sor              | 128 ms                                                 | 94.9 ms: 1.35x faster                                      |
| sympy_sum                | 92.2 ms                                                | 69.2 ms: 1.33x faster                                      |
| deepcopy                 | 272 us                                                 | 204 us: 1.33x faster                                       |
| pyflate                  | 427 ms                                                 | 321 ms: 1.33x faster                                       |
| thrift                   | 572 us                                                 | 435 us: 1.31x faster                                       |
| coroutines               | 20.7 ms                                                | 15.8 ms: 1.31x faster                                      |
| json_dumps               | 8.11 ms                                                | 6.23 ms: 1.30x faster                                      |
| tornado_http             | 86.7 ms                                                | 66.7 ms: 1.30x faster                                      |
| dulwich_log              | 35.3 ms                                                | 27.6 ms: 1.28x faster                                      |
| deepcopy_reduce          | 2.33 us                                                | 1.82 us: 1.28x faster                                      |
| sympy_integrate          | 13.1 ms                                                | 10.3 ms: 1.27x faster                                      |
| sympy_str                | 165 ms                                                 | 131 ms: 1.26x faster                                       |
| gunicorn                 | 1.30 ms                                                | 1.04 ms: 1.26x faster                                      |
| xml_etree_process        | 46.5 ms                                                | 37.1 ms: 1.26x faster                                      |
| genshi_text              | 17.3 ms                                                | 13.9 ms: 1.25x faster                                      |
| scimark_fft              | 224 ms                                                 | 181 ms: 1.24x faster                                       |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.29 sec: 1.24x faster                                     |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.77 ms: 1.23x faster                                      |
| aiohttp                  | 1.22 ms                                                | 997 us: 1.23x faster                                       |
| nqueens                  | 63.8 ms                                                | 52.2 ms: 1.22x faster                                      |
| fannkuch                 | 303 ms                                                 | 248 ms: 1.22x faster                                       |
| docutils                 | 1.73 sec                                               | 1.44 sec: 1.21x faster                                     |
| sympy_expand             | 269 ms                                                 | 226 ms: 1.19x faster                                       |
| 2to3                     | 192 ms                                                 | 161 ms: 1.19x faster                                       |
| sqlglot_optimize         | 36.8 ms                                                | 30.9 ms: 1.19x faster                                      |
| bench_thread_pool        | 527 us                                                 | 447 us: 1.18x faster                                       |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                       |
| tomli_loads              | 1.71 sec                                               | 1.47 sec: 1.16x faster                                     |
| sqlglot_normalize        | 190 ms                                                 | 166 ms: 1.15x faster                                       |
| dask                     | 253 ms                                                 | 221 ms: 1.14x faster                                       |
| genshi_xml               | 33.8 ms                                                | 29.9 ms: 1.13x faster                                      |
| meteor_contest           | 77.7 ms                                                | 70.3 ms: 1.11x faster                                      |
| mdp                      | 1.63 sec                                               | 1.53 sec: 1.06x faster                                     |
| json                     | 3.08 ms                                                | 2.93 ms: 1.05x faster                                      |
| pathlib                  | 24.5 ms                                                | 23.3 ms: 1.05x faster                                      |
| xml_etree_parse          | 108 ms                                                 | 106 ms: 1.02x faster                                       |
| xml_etree_generate       | 53.5 ms                                                | 52.7 ms: 1.02x faster                                      |
| xml_etree_iterparse      | 72.1 ms                                                | 71.5 ms: 1.01x faster                                      |
| regex_v8                 | 17.1 ms                                                | 17.3 ms: 1.01x slower                                      |
| json_loads               | 16.4 us                                                | 16.8 us: 1.02x slower                                      |
| gc_traversal             | 2.36 ms                                                | 2.45 ms: 1.04x slower                                      |
| unpickle                 | 8.80 us                                                | 9.12 us: 1.04x slower                                      |
| create_gc_cycles         | 860 us                                                 | 897 us: 1.04x slower                                       |
| regex_effbot             | 2.46 ms                                                | 2.58 ms: 1.05x slower                                      |
| sqlite_synth             | 1.46 us                                                | 1.55 us: 1.06x slower                                      |
| unpickle_list            | 2.69 us                                                | 2.88 us: 1.07x slower                                      |
| pickle                   | 6.97 us                                                | 7.48 us: 1.07x slower                                      |
| pickle_dict              | 17.0 us                                                | 18.3 us: 1.08x slower                                      |
| pickle_list              | 2.74 us                                                | 2.96 us: 1.08x slower                                      |
| coverage                 | 41.5 ms                                                | 45.0 ms: 1.08x slower                                      |
| async_generators         | 231 ms                                                 | 281 ms: 1.21x slower                                       |
| bench_mp_pool            | 37.4 ms                                                | 47.2 ms: 1.26x slower                                      |
| telco                    | 3.49 ms                                                | 4.60 ms: 1.32x slower                                      |
| flaskblogging            | 2.65 ms                                                | 3.61 ms: 1.36x slower                                      |
| python_startup           | 10.9 ms                                                | 15.2 ms: 1.39x slower                                      |
| python_startup_no_site   | 7.91 ms                                                | 12.3 ms: 1.56x slower                                      |
| Geometric mean           | (ref)                                                  | 1.27x faster                                               |

Benchmark hidden because not significant (2): asyncio_websockets, pidigits
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.18x