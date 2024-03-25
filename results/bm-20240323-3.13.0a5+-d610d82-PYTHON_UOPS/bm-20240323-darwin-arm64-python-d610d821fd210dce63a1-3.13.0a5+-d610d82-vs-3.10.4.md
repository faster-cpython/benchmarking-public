# Results vs. 3.10.4

- fork: python
- ref: d610d821fd210dce63a1
- machine: darwin-arm64
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.13x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 177 ms: 1.08x faster                                                   |
| chameleon      | 6.26 ms                                                | 4.71 ms: 1.33x faster                                                  |
| docutils       | 1.73 sec                                               | 1.60 sec: 1.08x faster                                                 |
| html5lib       | 42.4 ms                                                | 35.0 ms: 1.21x faster                                                  |
| Geometric mean | (ref)                                                  | 1.15x faster                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization  | 474 ms                                                 | 264 ms: 1.80x faster                                                   |
| async_tree_none         | 388 ms                                                 | 230 ms: 1.69x faster                                                   |
| async_tree_io           | 980 ms                                                 | 583 ms: 1.68x faster                                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 466 ms: 1.39x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.63x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 86.0 ms: 1.08x faster                                                  |
| float          | 69.0 ms                                                | 66.6 ms: 1.04x faster                                                  |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 174 ms                                                 | 151 ms: 1.15x faster                                                   |
| regex_compile  | 95.3 ms                                                | 95.0 ms: 1.00x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.55 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 190 us: 1.48x faster                                                   |
| json_dumps           | 8.11 ms                                                | 6.48 ms: 1.25x faster                                                  |
| xml_etree_process    | 46.5 ms                                                | 39.8 ms: 1.17x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 98.9 ms: 1.09x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 186 us: 1.04x faster                                                   |
| tomli_loads          | 1.71 sec                                               | 1.68 sec: 1.02x faster                                                 |
| json_loads           | 16.4 us                                                | 17.0 us: 1.03x slower                                                  |
| unpickle             | 8.80 us                                                | 9.14 us: 1.04x slower                                                  |
| pickle               | 6.97 us                                                | 7.25 us: 1.04x slower                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 75.2 ms: 1.04x slower                                                  |
| pickle_dict          | 17.0 us                                                | 18.1 us: 1.07x slower                                                  |
| pickle_list          | 2.74 us                                                | 2.96 us: 1.08x slower                                                  |
| xml_etree_generate   | 53.5 ms                                                | 57.9 ms: 1.08x slower                                                  |
| unpickle_list        | 2.69 us                                                | 3.07 us: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 14.8 ms: 1.36x slower                                                  |
| python_startup_no_site | 7.91 ms                                                | 13.0 ms: 1.65x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.50x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 26.4 ms                                                | 22.4 ms: 1.18x faster                                                  |
| genshi_text     | 17.3 ms                                                | 16.5 ms: 1.05x faster                                                  |
| mako            | 9.87 ms                                                | 9.45 ms: 1.04x faster                                                  |
| genshi_xml      | 33.8 ms                                                | 34.5 ms: 1.02x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 72.4 us: 4.46x faster                                                  |
| deltablue                | 4.91 ms                                                | 2.60 ms: 1.89x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 264 ms: 1.80x faster                                                   |
| logging_silent           | 117 ns                                                 | 68.2 ns: 1.72x faster                                                  |
| async_tree_none          | 388 ms                                                 | 230 ms: 1.69x faster                                                   |
| async_tree_io            | 980 ms                                                 | 583 ms: 1.68x faster                                                   |
| asyncio_tcp              | 659 ms                                                 | 409 ms: 1.61x faster                                                   |
| pylint                   | 277 ms                                                 | 181 ms: 1.53x faster                                                   |
| sqlglot_parse            | 1.24 ms                                                | 819 us: 1.52x faster                                                   |
| raytrace                 | 301 ms                                                 | 200 ms: 1.51x faster                                                   |
| pickle_pure_python       | 281 us                                                 | 190 us: 1.48x faster                                                   |
| richards_super           | 57.8 ms                                                | 39.2 ms: 1.48x faster                                                  |
| chaos                    | 65.8 ms                                                | 45.0 ms: 1.46x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 988 us: 1.46x faster                                                   |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 466 ms: 1.39x faster                                                   |
| richards                 | 48.7 ms                                                | 36.0 ms: 1.35x faster                                                  |
| chameleon                | 6.26 ms                                                | 4.71 ms: 1.33x faster                                                  |
| logging_format           | 4.83 us                                                | 3.69 us: 1.31x faster                                                  |
| logging_simple           | 4.45 us                                                | 3.41 us: 1.30x faster                                                  |
| go                       | 151 ms                                                 | 116 ms: 1.30x faster                                                   |
| thrift                   | 572 us                                                 | 441 us: 1.30x faster                                                   |
| crypto_pyaes             | 71.8 ms                                                | 56.8 ms: 1.27x faster                                                  |
| deepcopy_memo            | 34.7 us                                                | 27.7 us: 1.25x faster                                                  |
| json_dumps               | 8.11 ms                                                | 6.48 ms: 1.25x faster                                                  |
| pycparser                | 877 ms                                                 | 702 ms: 1.25x faster                                                   |
| mypy2                    | 607 ms                                                 | 495 ms: 1.23x faster                                                   |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.31 sec: 1.22x faster                                                 |
| deepcopy                 | 272 us                                                 | 223 us: 1.22x faster                                                   |
| html5lib                 | 42.4 ms                                                | 35.0 ms: 1.21x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 1.92 us: 1.21x faster                                                  |
| create_gc_cycles         | 860 us                                                 | 718 us: 1.20x faster                                                   |
| dulwich_log              | 35.3 ms                                                | 29.8 ms: 1.18x faster                                                  |
| django_template          | 26.4 ms                                                | 22.4 ms: 1.18x faster                                                  |
| generators               | 32.3 ms                                                | 27.4 ms: 1.18x faster                                                  |
| coroutines               | 20.7 ms                                                | 17.6 ms: 1.18x faster                                                  |
| xml_etree_process        | 46.5 ms                                                | 39.8 ms: 1.17x faster                                                  |
| regex_dna                | 174 ms                                                 | 151 ms: 1.15x faster                                                   |
| sympy_sum                | 92.2 ms                                                | 80.9 ms: 1.14x faster                                                  |
| scimark_sor              | 128 ms                                                 | 113 ms: 1.13x faster                                                   |
| dask                     | 253 ms                                                 | 226 ms: 1.12x faster                                                   |
| sympy_integrate          | 13.1 ms                                                | 11.8 ms: 1.11x faster                                                  |
| gunicorn                 | 1.30 ms                                                | 1.17 ms: 1.11x faster                                                  |
| unpack_sequence          | 39.0 ns                                                | 35.3 ns: 1.11x faster                                                  |
| sympy_str                | 165 ms                                                 | 151 ms: 1.09x faster                                                   |
| sympy_expand             | 269 ms                                                 | 246 ms: 1.09x faster                                                   |
| xml_etree_parse          | 108 ms                                                 | 98.9 ms: 1.09x faster                                                  |
| pprint_safe_repr         | 641 ms                                                 | 588 ms: 1.09x faster                                                   |
| aiohttp                  | 1.22 ms                                                | 1.12 ms: 1.09x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 1.20 sec: 1.09x faster                                                 |
| docutils                 | 1.73 sec                                               | 1.60 sec: 1.08x faster                                                 |
| 2to3                     | 192 ms                                                 | 177 ms: 1.08x faster                                                   |
| scimark_monte_carlo      | 65.6 ms                                                | 60.6 ms: 1.08x faster                                                  |
| nbody                    | 93.0 ms                                                | 86.0 ms: 1.08x faster                                                  |
| comprehensions           | 16.9 us                                                | 16.0 us: 1.06x faster                                                  |
| genshi_text              | 17.3 ms                                                | 16.5 ms: 1.05x faster                                                  |
| mako                     | 9.87 ms                                                | 9.45 ms: 1.04x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 186 us: 1.04x faster                                                   |
| pyflate                  | 427 ms                                                 | 409 ms: 1.04x faster                                                   |
| json                     | 3.08 ms                                                | 2.96 ms: 1.04x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 508 us: 1.04x faster                                                   |
| float                    | 69.0 ms                                                | 66.6 ms: 1.04x faster                                                  |
| scimark_lu               | 103 ms                                                 | 99.8 ms: 1.03x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 36.0 ms: 1.02x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.68 sec: 1.02x faster                                                 |
| sqlglot_normalize        | 190 ms                                                 | 188 ms: 1.01x faster                                                   |
| hexiom                   | 6.19 ms                                                | 6.15 ms: 1.01x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.62 sec: 1.00x faster                                                 |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                                   |
| regex_compile            | 95.3 ms                                                | 95.0 ms: 1.00x faster                                                  |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| gc_traversal             | 2.36 ms                                                | 2.40 ms: 1.02x slower                                                  |
| genshi_xml               | 33.8 ms                                                | 34.5 ms: 1.02x slower                                                  |
| json_loads               | 16.4 us                                                | 17.0 us: 1.03x slower                                                  |
| regex_effbot             | 2.46 ms                                                | 2.55 ms: 1.04x slower                                                  |
| unpickle                 | 8.80 us                                                | 9.14 us: 1.04x slower                                                  |
| pickle                   | 6.97 us                                                | 7.25 us: 1.04x slower                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 75.2 ms: 1.04x slower                                                  |
| meteor_contest           | 77.7 ms                                                | 81.3 ms: 1.05x slower                                                  |
| pickle_dict              | 17.0 us                                                | 18.1 us: 1.07x slower                                                  |
| pickle_list              | 2.74 us                                                | 2.96 us: 1.08x slower                                                  |
| xml_etree_generate       | 53.5 ms                                                | 57.9 ms: 1.08x slower                                                  |
| spectral_norm            | 94.8 ms                                                | 103 ms: 1.08x slower                                                   |
| scimark_fft              | 224 ms                                                 | 245 ms: 1.09x slower                                                   |
| sqlite_synth             | 1.46 us                                                | 1.63 us: 1.12x slower                                                  |
| coverage                 | 41.5 ms                                                | 47.0 ms: 1.13x slower                                                  |
| unpickle_list            | 2.69 us                                                | 3.07 us: 1.14x slower                                                  |
| nqueens                  | 63.8 ms                                                | 73.1 ms: 1.15x slower                                                  |
| fannkuch                 | 303 ms                                                 | 349 ms: 1.15x slower                                                   |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.98 ms: 1.16x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 46.0 ms: 1.23x slower                                                  |
| async_generators         | 231 ms                                                 | 299 ms: 1.29x slower                                                   |
| python_startup           | 10.9 ms                                                | 14.8 ms: 1.36x slower                                                  |
| telco                    | 3.49 ms                                                | 4.78 ms: 1.37x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 13.0 ms: 1.65x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.13x faster                                                           |

Benchmark hidden because not significant (3): tornado_http, regex_v8, pathlib
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (12) of results/bm-20240323-3.13.0a5+-d610d82-PYTHON_UOPS/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x


# Memory

- memory change: 1.15x