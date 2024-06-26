# Results vs. 3.10.4

- fork: python
- ref: bfc57d43d8766120ba0c
- machine: darwin-arm64
- commit hash: bfc57d4
- commit date: 2024-03-29
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240329-darwin-arm64-python-bfc57d43d8766120ba0c-3.13.0a5+-bfc57d4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 165 ms: 1.16x faster                                                   |
| chameleon      | 6.26 ms                                                | 4.60 ms: 1.36x faster                                                  |
| docutils       | 1.73 sec                                               | 1.48 sec: 1.17x faster                                                 |
| html5lib       | 42.4 ms                                                | 34.0 ms: 1.25x faster                                                  |
| tornado_http   | 86.7 ms                                                | 76.3 ms: 1.14x faster                                                  |
| Geometric mean | (ref)                                                  | 1.21x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240329-darwin-arm64-python-bfc57d43d8766120ba0c-3.13.0a5+-bfc57d4 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization  | 474 ms                                                 | 262 ms: 1.81x faster                                                   |
| async_tree_none         | 388 ms                                                 | 218 ms: 1.78x faster                                                   |
| async_tree_io           | 980 ms                                                 | 558 ms: 1.76x faster                                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 456 ms: 1.42x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.68x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240329-darwin-arm64-python-bfc57d43d8766120ba0c-3.13.0a5+-bfc57d4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 66.1 ms: 1.41x faster                                                  |
| float          | 69.0 ms                                                | 51.9 ms: 1.33x faster                                                  |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.23x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240329-darwin-arm64-python-bfc57d43d8766120ba0c-3.13.0a5+-bfc57d4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 69.7 ms: 1.37x faster                                                  |
| regex_dna      | 174 ms                                                 | 152 ms: 1.15x faster                                                   |
| regex_v8       | 17.1 ms                                                | 17.0 ms: 1.01x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.59 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240329-darwin-arm64-python-bfc57d43d8766120ba0c-3.13.0a5+-bfc57d4 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 185 us: 1.52x faster                                                   |
| json_dumps           | 8.11 ms                                                | 6.25 ms: 1.30x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 150 us: 1.30x faster                                                   |
| xml_etree_process    | 46.5 ms                                                | 37.8 ms: 1.23x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.49 sec: 1.15x faster                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 72.8 ms: 1.01x slower                                                  |
| xml_etree_generate   | 53.5 ms                                                | 55.2 ms: 1.03x slower                                                  |
| json_loads           | 16.4 us                                                | 17.1 us: 1.04x slower                                                  |
| unpickle             | 8.80 us                                                | 9.27 us: 1.05x slower                                                  |
| pickle_dict          | 17.0 us                                                | 18.1 us: 1.07x slower                                                  |
| pickle               | 6.97 us                                                | 7.48 us: 1.07x slower                                                  |
| pickle_list          | 2.74 us                                                | 3.00 us: 1.09x slower                                                  |
| unpickle_list        | 2.69 us                                                | 3.04 us: 1.13x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240329-darwin-arm64-python-bfc57d43d8766120ba0c-3.13.0a5+-bfc57d4 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 11.9 ms: 1.10x slower                                                  |
| python_startup_no_site | 7.91 ms                                                | 10.2 ms: 1.29x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.19x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240329-darwin-arm64-python-bfc57d43d8766120ba0c-3.13.0a5+-bfc57d4 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.95 ms: 1.42x faster                                                  |
| django_template | 26.4 ms                                                | 20.7 ms: 1.27x faster                                                  |
| genshi_text     | 17.3 ms                                                | 14.6 ms: 1.19x faster                                                  |
| genshi_xml      | 33.8 ms                                                | 31.5 ms: 1.07x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.23x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240329-darwin-arm64-python-bfc57d43d8766120ba0c-3.13.0a5+-bfc57d4 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 70.8 us: 4.56x faster                                                  |
| deltablue                | 4.91 ms                                                | 2.30 ms: 2.14x faster                                                  |
| raytrace                 | 301 ms                                                 | 157 ms: 1.92x faster                                                   |
| pylint                   | 277 ms                                                 | 149 ms: 1.86x faster                                                   |
| async_tree_memoization   | 474 ms                                                 | 262 ms: 1.81x faster                                                   |
| chaos                    | 65.8 ms                                                | 36.5 ms: 1.80x faster                                                  |
| logging_silent           | 117 ns                                                 | 65.9 ns: 1.78x faster                                                  |
| async_tree_none          | 388 ms                                                 | 218 ms: 1.78x faster                                                   |
| async_tree_io            | 980 ms                                                 | 558 ms: 1.76x faster                                                   |
| richards_super           | 57.8 ms                                                | 34.9 ms: 1.66x faster                                                  |
| comprehensions           | 16.9 us                                                | 10.2 us: 1.65x faster                                                  |
| sqlglot_parse            | 1.24 ms                                                | 756 us: 1.65x faster                                                   |
| asyncio_tcp              | 659 ms                                                 | 417 ms: 1.58x faster                                                   |
| mypy2                    | 607 ms                                                 | 385 ms: 1.58x faster                                                   |
| sqlglot_transpile        | 1.44 ms                                                | 918 us: 1.57x faster                                                   |
| richards                 | 48.7 ms                                                | 31.3 ms: 1.56x faster                                                  |
| crypto_pyaes             | 71.8 ms                                                | 47.2 ms: 1.52x faster                                                  |
| pickle_pure_python       | 281 us                                                 | 185 us: 1.52x faster                                                   |
| go                       | 151 ms                                                 | 101 ms: 1.50x faster                                                   |
| scimark_lu               | 103 ms                                                 | 68.9 ms: 1.49x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 44.6 ms: 1.47x faster                                                  |
| deepcopy_memo            | 34.7 us                                                | 23.9 us: 1.45x faster                                                  |
| unpack_sequence          | 39.0 ns                                                | 26.9 ns: 1.45x faster                                                  |
| hexiom                   | 6.19 ms                                                | 4.27 ms: 1.45x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 456 ms: 1.42x faster                                                   |
| mako                     | 9.87 ms                                                | 6.95 ms: 1.42x faster                                                  |
| nbody                    | 93.0 ms                                                | 66.1 ms: 1.41x faster                                                  |
| regex_compile            | 95.3 ms                                                | 69.7 ms: 1.37x faster                                                  |
| chameleon                | 6.26 ms                                                | 4.60 ms: 1.36x faster                                                  |
| logging_format           | 4.83 us                                                | 3.62 us: 1.33x faster                                                  |
| logging_simple           | 4.45 us                                                | 3.34 us: 1.33x faster                                                  |
| spectral_norm            | 94.8 ms                                                | 71.3 ms: 1.33x faster                                                  |
| float                    | 69.0 ms                                                | 51.9 ms: 1.33x faster                                                  |
| pycparser                | 877 ms                                                 | 660 ms: 1.33x faster                                                   |
| pprint_pformat           | 1.30 sec                                               | 989 ms: 1.32x faster                                                   |
| pprint_safe_repr         | 641 ms                                                 | 486 ms: 1.32x faster                                                   |
| sympy_sum                | 92.2 ms                                                | 70.0 ms: 1.32x faster                                                  |
| pyflate                  | 427 ms                                                 | 329 ms: 1.30x faster                                                   |
| json_dumps               | 8.11 ms                                                | 6.25 ms: 1.30x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 150 us: 1.30x faster                                                   |
| thrift                   | 572 us                                                 | 442 us: 1.30x faster                                                   |
| django_template          | 26.4 ms                                                | 20.7 ms: 1.27x faster                                                  |
| scimark_sor              | 128 ms                                                 | 101 ms: 1.27x faster                                                   |
| sympy_integrate          | 13.1 ms                                                | 10.4 ms: 1.27x faster                                                  |
| deepcopy                 | 272 us                                                 | 215 us: 1.26x faster                                                   |
| sympy_str                | 165 ms                                                 | 132 ms: 1.25x faster                                                   |
| html5lib                 | 42.4 ms                                                | 34.0 ms: 1.25x faster                                                  |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.30 sec: 1.23x faster                                                 |
| xml_etree_process        | 46.5 ms                                                | 37.8 ms: 1.23x faster                                                  |
| dulwich_log              | 35.3 ms                                                | 28.9 ms: 1.22x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 1.91 us: 1.22x faster                                                  |
| coroutines               | 20.7 ms                                                | 17.0 ms: 1.22x faster                                                  |
| genshi_text              | 17.3 ms                                                | 14.6 ms: 1.19x faster                                                  |
| gunicorn                 | 1.30 ms                                                | 1.10 ms: 1.18x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.48 sec: 1.17x faster                                                 |
| generators               | 32.3 ms                                                | 27.7 ms: 1.17x faster                                                  |
| 2to3                     | 192 ms                                                 | 165 ms: 1.16x faster                                                   |
| dask                     | 253 ms                                                 | 219 ms: 1.16x faster                                                   |
| scimark_fft              | 224 ms                                                 | 195 ms: 1.15x faster                                                   |
| fannkuch                 | 303 ms                                                 | 263 ms: 1.15x faster                                                   |
| regex_dna                | 174 ms                                                 | 152 ms: 1.15x faster                                                   |
| aiohttp                  | 1.22 ms                                                | 1.07 ms: 1.15x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.49 sec: 1.15x faster                                                 |
| sqlglot_optimize         | 36.8 ms                                                | 32.1 ms: 1.14x faster                                                  |
| tornado_http             | 86.7 ms                                                | 76.3 ms: 1.14x faster                                                  |
| nqueens                  | 63.8 ms                                                | 56.2 ms: 1.13x faster                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.05 ms: 1.12x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 476 us: 1.11x faster                                                   |
| sqlglot_normalize        | 190 ms                                                 | 172 ms: 1.10x faster                                                   |
| meteor_contest           | 77.7 ms                                                | 71.3 ms: 1.09x faster                                                  |
| genshi_xml               | 33.8 ms                                                | 31.5 ms: 1.07x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.53 sec: 1.06x faster                                                 |
| json                     | 3.08 ms                                                | 2.97 ms: 1.04x faster                                                  |
| create_gc_cycles         | 860 us                                                 | 835 us: 1.03x faster                                                   |
| regex_v8                 | 17.1 ms                                                | 17.0 ms: 1.01x faster                                                  |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| xml_etree_iterparse      | 72.1 ms                                                | 72.8 ms: 1.01x slower                                                  |
| gc_traversal             | 2.36 ms                                                | 2.43 ms: 1.03x slower                                                  |
| xml_etree_generate       | 53.5 ms                                                | 55.2 ms: 1.03x slower                                                  |
| json_loads               | 16.4 us                                                | 17.1 us: 1.04x slower                                                  |
| unpickle                 | 8.80 us                                                | 9.27 us: 1.05x slower                                                  |
| regex_effbot             | 2.46 ms                                                | 2.59 ms: 1.06x slower                                                  |
| pickle_dict              | 17.0 us                                                | 18.1 us: 1.07x slower                                                  |
| pickle                   | 6.97 us                                                | 7.48 us: 1.07x slower                                                  |
| sqlite_synth             | 1.46 us                                                | 1.57 us: 1.08x slower                                                  |
| pickle_list              | 2.74 us                                                | 3.00 us: 1.09x slower                                                  |
| python_startup           | 10.9 ms                                                | 11.9 ms: 1.10x slower                                                  |
| coverage                 | 41.5 ms                                                | 46.8 ms: 1.13x slower                                                  |
| unpickle_list            | 2.69 us                                                | 3.04 us: 1.13x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 42.9 ms: 1.15x slower                                                  |
| async_generators         | 231 ms                                                 | 286 ms: 1.24x slower                                                   |
| python_startup_no_site   | 7.91 ms                                                | 10.2 ms: 1.29x slower                                                  |
| telco                    | 3.49 ms                                                | 4.54 ms: 1.30x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.24x faster                                                           |

Benchmark hidden because not significant (4): sympy_expand, asyncio_websockets, pathlib, xml_etree_parse
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (12) of results/bm-20240329-3.13.0a5+-bfc57d4/bm-20240329-darwin-arm64-python-bfc57d43d8766120ba0c-3.13.0a5+-bfc57d4.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: 1.14x