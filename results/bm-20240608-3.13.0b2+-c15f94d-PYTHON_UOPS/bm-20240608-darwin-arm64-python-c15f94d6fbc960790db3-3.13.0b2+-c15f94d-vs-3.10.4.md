# Results vs. 3.10.4

- fork: python
- ref: c15f94d6fbc960790db3
- machine: darwin-arm64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.11x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.71x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 181 ms: 1.06x faster                                                   |
| chameleon      | 6.26 ms                                                | 4.97 ms: 1.26x faster                                                  |
| docutils       | 1.73 sec                                               | 1.66 sec: 1.04x faster                                                 |
| html5lib       | 42.4 ms                                                | 33.3 ms: 1.27x faster                                                  |
| tornado_http   | 86.7 ms                                                | 69.4 ms: 1.25x faster                                                  |
| Geometric mean | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 221 ms: 1.76x faster                                                   |
| async_tree_memoization  | 474 ms                                                 | 269 ms: 1.76x faster                                                   |
| async_tree_io           | 980 ms                                                 | 568 ms: 1.72x faster                                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 476 ms: 1.36x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.64x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 76.8 ms: 1.21x faster                                                  |
| float          | 69.0 ms                                                | 60.7 ms: 1.14x faster                                                  |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                                   |
| regex_compile  | 95.3 ms                                                | 96.0 ms: 1.01x slower                                                  |
| regex_v8       | 17.1 ms                                                | 17.6 ms: 1.02x slower                                                  |
| regex_effbot   | 2.46 ms                                                | 2.58 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 226 us: 1.24x faster                                                   |
| json_dumps           | 8.11 ms                                                | 6.60 ms: 1.23x faster                                                  |
| xml_etree_process    | 46.5 ms                                                | 41.2 ms: 1.13x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 175 us: 1.11x faster                                                   |
| tomli_loads          | 1.71 sec                                               | 1.63 sec: 1.05x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                                   |
| json_loads           | 16.4 us                                                | 16.9 us: 1.03x slower                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 76.0 ms: 1.05x slower                                                  |
| unpickle             | 8.80 us                                                | 9.31 us: 1.06x slower                                                  |
| pickle_dict          | 17.0 us                                                | 18.2 us: 1.07x slower                                                  |
| pickle               | 6.97 us                                                | 7.52 us: 1.08x slower                                                  |
| unpickle_list        | 2.69 us                                                | 2.94 us: 1.09x slower                                                  |
| pickle_list          | 2.74 us                                                | 3.00 us: 1.10x slower                                                  |
| xml_etree_generate   | 53.5 ms                                                | 59.0 ms: 1.10x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 14.3 ms: 1.31x slower                                                  |
| python_startup_no_site | 7.91 ms                                                | 11.4 ms: 1.44x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.37x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 26.4 ms                                                | 23.6 ms: 1.12x faster                                                  |
| mako            | 9.87 ms                                                | 8.85 ms: 1.12x faster                                                  |
| genshi_xml      | 33.8 ms                                                | 35.9 ms: 1.06x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 106 us: 3.04x faster                                                   |
| async_tree_none          | 388 ms                                                 | 221 ms: 1.76x faster                                                   |
| async_tree_memoization   | 474 ms                                                 | 269 ms: 1.76x faster                                                   |
| async_tree_io            | 980 ms                                                 | 568 ms: 1.72x faster                                                   |
| deltablue                | 4.91 ms                                                | 2.94 ms: 1.67x faster                                                  |
| raytrace                 | 301 ms                                                 | 180 ms: 1.67x faster                                                   |
| asyncio_tcp              | 659 ms                                                 | 421 ms: 1.57x faster                                                   |
| pylint                   | 277 ms                                                 | 190 ms: 1.45x faster                                                   |
| richards_super           | 57.8 ms                                                | 40.8 ms: 1.42x faster                                                  |
| mypy2                    | 607 ms                                                 | 428 ms: 1.42x faster                                                   |
| chaos                    | 65.8 ms                                                | 46.4 ms: 1.42x faster                                                  |
| logging_simple           | 4.45 us                                                | 3.16 us: 1.41x faster                                                  |
| logging_format           | 4.83 us                                                | 3.46 us: 1.40x faster                                                  |
| generators               | 32.3 ms                                                | 23.4 ms: 1.38x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 476 ms: 1.36x faster                                                   |
| sqlglot_parse            | 1.24 ms                                                | 952 us: 1.31x faster                                                   |
| richards                 | 48.7 ms                                                | 37.4 ms: 1.30x faster                                                  |
| thrift                   | 572 us                                                 | 441 us: 1.30x faster                                                   |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.24 sec: 1.29x faster                                                 |
| go                       | 151 ms                                                 | 117 ms: 1.28x faster                                                   |
| coroutines               | 20.7 ms                                                | 16.2 ms: 1.28x faster                                                  |
| html5lib                 | 42.4 ms                                                | 33.3 ms: 1.27x faster                                                  |
| chameleon                | 6.26 ms                                                | 4.97 ms: 1.26x faster                                                  |
| tornado_http             | 86.7 ms                                                | 69.4 ms: 1.25x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 1.16 ms: 1.25x faster                                                  |
| pickle_pure_python       | 281 us                                                 | 226 us: 1.24x faster                                                   |
| logging_silent           | 117 ns                                                 | 94.6 ns: 1.24x faster                                                  |
| json_dumps               | 8.11 ms                                                | 6.60 ms: 1.23x faster                                                  |
| pycparser                | 877 ms                                                 | 723 ms: 1.21x faster                                                   |
| nbody                    | 93.0 ms                                                | 76.8 ms: 1.21x faster                                                  |
| dulwich_log              | 35.3 ms                                                | 29.5 ms: 1.20x faster                                                  |
| scimark_sor              | 128 ms                                                 | 107 ms: 1.20x faster                                                   |
| crypto_pyaes             | 71.8 ms                                                | 60.8 ms: 1.18x faster                                                  |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                                   |
| gunicorn                 | 1.30 ms                                                | 1.12 ms: 1.16x faster                                                  |
| aiohttp                  | 1.22 ms                                                | 1.06 ms: 1.16x faster                                                  |
| float                    | 69.0 ms                                                | 60.7 ms: 1.14x faster                                                  |
| xml_etree_process        | 46.5 ms                                                | 41.2 ms: 1.13x faster                                                  |
| django_template          | 26.4 ms                                                | 23.6 ms: 1.12x faster                                                  |
| mako                     | 9.87 ms                                                | 8.85 ms: 1.12x faster                                                  |
| dask                     | 253 ms                                                 | 227 ms: 1.11x faster                                                   |
| unpickle_pure_python     | 194 us                                                 | 175 us: 1.11x faster                                                   |
| pprint_safe_repr         | 641 ms                                                 | 579 ms: 1.11x faster                                                   |
| pprint_pformat           | 1.30 sec                                               | 1.18 sec: 1.10x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 2.12 us: 1.10x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 84.9 ms: 1.09x faster                                                  |
| deepcopy                 | 272 us                                                 | 251 us: 1.08x faster                                                   |
| pyflate                  | 427 ms                                                 | 395 ms: 1.08x faster                                                   |
| pathlib                  | 24.5 ms                                                | 22.7 ms: 1.08x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 60.8 ms: 1.08x faster                                                  |
| deepcopy_memo            | 34.7 us                                                | 32.6 us: 1.06x faster                                                  |
| 2to3                     | 192 ms                                                 | 181 ms: 1.06x faster                                                   |
| scimark_lu               | 103 ms                                                 | 97.1 ms: 1.06x faster                                                  |
| sympy_integrate          | 13.1 ms                                                | 12.5 ms: 1.05x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.63 sec: 1.05x faster                                                 |
| xml_etree_parse          | 108 ms                                                 | 103 ms: 1.05x faster                                                   |
| hexiom                   | 6.19 ms                                                | 5.92 ms: 1.05x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.56 sec: 1.05x faster                                                 |
| docutils                 | 1.73 sec                                               | 1.66 sec: 1.04x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 92.1 ms: 1.03x faster                                                  |
| sympy_expand             | 269 ms                                                 | 264 ms: 1.02x faster                                                   |
| json                     | 3.08 ms                                                | 3.03 ms: 1.02x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 522 us: 1.01x faster                                                   |
| sympy_str                | 165 ms                                                 | 164 ms: 1.01x faster                                                   |
| scimark_fft              | 224 ms                                                 | 223 ms: 1.01x faster                                                   |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| sqlglot_optimize         | 36.8 ms                                                | 37.0 ms: 1.01x slower                                                  |
| regex_compile            | 95.3 ms                                                | 96.0 ms: 1.01x slower                                                  |
| meteor_contest           | 77.7 ms                                                | 78.6 ms: 1.01x slower                                                  |
| fannkuch                 | 303 ms                                                 | 308 ms: 1.02x slower                                                   |
| comprehensions           | 16.9 us                                                | 17.3 us: 1.02x slower                                                  |
| regex_v8                 | 17.1 ms                                                | 17.6 ms: 1.02x slower                                                  |
| json_loads               | 16.4 us                                                | 16.9 us: 1.03x slower                                                  |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                  |
| regex_effbot             | 2.46 ms                                                | 2.58 ms: 1.05x slower                                                  |
| create_gc_cycles         | 860 us                                                 | 903 us: 1.05x slower                                                   |
| xml_etree_iterparse      | 72.1 ms                                                | 76.0 ms: 1.05x slower                                                  |
| nqueens                  | 63.8 ms                                                | 67.5 ms: 1.06x slower                                                  |
| unpickle                 | 8.80 us                                                | 9.31 us: 1.06x slower                                                  |
| genshi_xml               | 33.8 ms                                                | 35.9 ms: 1.06x slower                                                  |
| pickle_dict              | 17.0 us                                                | 18.2 us: 1.07x slower                                                  |
| pickle                   | 6.97 us                                                | 7.52 us: 1.08x slower                                                  |
| unpickle_list            | 2.69 us                                                | 2.94 us: 1.09x slower                                                  |
| pickle_list              | 2.74 us                                                | 3.00 us: 1.10x slower                                                  |
| xml_etree_generate       | 53.5 ms                                                | 59.0 ms: 1.10x slower                                                  |
| sqlite_synth             | 1.46 us                                                | 1.62 us: 1.11x slower                                                  |
| coverage                 | 41.5 ms                                                | 46.0 ms: 1.11x slower                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.86 ms: 1.13x slower                                                  |
| flaskblogging            | 2.65 ms                                                | 3.28 ms: 1.24x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 47.4 ms: 1.27x slower                                                  |
| async_generators         | 231 ms                                                 | 294 ms: 1.27x slower                                                   |
| python_startup           | 10.9 ms                                                | 14.3 ms: 1.31x slower                                                  |
| telco                    | 3.49 ms                                                | 4.96 ms: 1.42x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 11.4 ms: 1.44x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.11x faster                                                           |

Benchmark hidden because not significant (2): genshi_text, asyncio_websockets
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (12) of results/bm-20240608-3.13.0b2+-c15f94d-PYTHON_UOPS/bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.71x