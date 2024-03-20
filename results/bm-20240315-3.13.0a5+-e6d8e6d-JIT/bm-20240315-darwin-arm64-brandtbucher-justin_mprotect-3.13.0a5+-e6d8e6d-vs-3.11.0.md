# Results vs. 3.11.0

- fork: brandtbucher
- ref: justin_mprotect
- machine: darwin-arm64
- commit hash: e6d8e6d
- commit date: 2024-03-15
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.48x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5+-e6d8e6d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 154 ms                                                 | 183 ms: 1.18x slower                                                    |
| chameleon      | 4.30 ms                                                | 4.84 ms: 1.13x slower                                                   |
| docutils       | 1.43 sec                                               | 1.52 sec: 1.07x slower                                                  |
| html5lib       | 33.0 ms                                                | 35.6 ms: 1.08x slower                                                   |
| tornado_http   | 69.1 ms                                                | 83.7 ms: 1.21x slower                                                   |
| Geometric mean | (ref)                                                  | 1.13x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5+-e6d8e6d |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 282 ms                                                 | 253 ms: 1.11x faster                                                    |
| async_tree_memoization_tg  | 352 ms                                                 | 323 ms: 1.09x faster                                                    |
| async_tree_io_tg           | 724 ms                                                 | 673 ms: 1.08x faster                                                    |
| async_tree_none_tg         | 276 ms                                                 | 261 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed_tg | 550 ms                                                 | 533 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed    | 519 ms                                                 | 523 ms: 1.01x slower                                                    |
| async_tree_io              | 697 ms                                                 | 706 ms: 1.01x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                            |

Benchmark hidden because not significant (1): async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5+-e6d8e6d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 280 ms                                                 | 282 ms: 1.01x slower                                                    |
| float          | 50.8 ms                                                | 53.0 ms: 1.04x slower                                                   |
| nbody          | 61.7 ms                                                | 70.4 ms: 1.14x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5+-e6d8e6d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 148 ms                                                 | 153 ms: 1.03x slower                                                    |
| regex_effbot   | 2.43 ms                                                | 2.63 ms: 1.08x slower                                                   |
| regex_v8       | 15.1 ms                                                | 17.3 ms: 1.14x slower                                                   |
| regex_compile  | 72.8 ms                                                | 85.2 ms: 1.17x slower                                                   |
| Geometric mean | (ref)                                                  | 1.10x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5+-e6d8e6d |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps           | 7.53 ms                                                | 6.49 ms: 1.16x faster                                                   |
| unpickle_pure_python | 149 us                                                 | 150 us: 1.01x slower                                                    |
| pickle_pure_python   | 191 us                                                 | 198 us: 1.03x slower                                                    |
| pickle               | 6.98 us                                                | 7.24 us: 1.04x slower                                                   |
| tomli_loads          | 1.27 sec                                               | 1.33 sec: 1.05x slower                                                  |
| xml_etree_parse      | 100 ms                                                 | 106 ms: 1.06x slower                                                    |
| pickle_dict          | 17.1 us                                                | 18.1 us: 1.06x slower                                                   |
| xml_etree_iterparse  | 68.3 ms                                                | 74.9 ms: 1.10x slower                                                   |
| unpickle             | 8.29 us                                                | 9.18 us: 1.11x slower                                                   |
| pickle_list          | 2.70 us                                                | 2.99 us: 1.11x slower                                                   |
| json_loads           | 15.3 us                                                | 17.1 us: 1.11x slower                                                   |
| xml_etree_process    | 33.6 ms                                                | 38.8 ms: 1.16x slower                                                   |
| unpickle_list        | 2.69 us                                                | 3.11 us: 1.16x slower                                                   |
| xml_etree_generate   | 45.8 ms                                                | 55.8 ms: 1.22x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.07x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5+-e6d8e6d |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                | 16.8 ms: 1.56x slower                                                   |
| python_startup_no_site | 8.57 ms                                                | 15.2 ms: 1.77x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.66x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5+-e6d8e6d |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 7.93 ms                                                | 6.72 ms: 1.18x faster                                                   |
| django_template | 20.1 ms                                                | 21.9 ms: 1.09x slower                                                   |
| genshi_text     | 14.4 ms                                                | 15.7 ms: 1.09x slower                                                   |
| genshi_xml      | 28.5 ms                                                | 34.2 ms: 1.20x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5+-e6d8e6d |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols   | 301 us                                                 | 72.0 us: 4.18x faster                                                   |
| asyncio_tcp                | 643 ms                                                 | 408 ms: 1.58x faster                                                    |
| pylint                     | 253 ms                                                 | 176 ms: 1.44x faster                                                    |
| chaos                      | 47.4 ms                                                | 40.1 ms: 1.18x faster                                                   |
| mako                       | 7.93 ms                                                | 6.72 ms: 1.18x faster                                                   |
| json_dumps                 | 7.53 ms                                                | 6.49 ms: 1.16x faster                                                   |
| comprehensions             | 14.4 us                                                | 12.5 us: 1.15x faster                                                   |
| async_tree_none            | 282 ms                                                 | 253 ms: 1.11x faster                                                    |
| sqlglot_parse              | 890 us                                                 | 814 us: 1.09x faster                                                    |
| async_tree_memoization_tg  | 352 ms                                                 | 323 ms: 1.09x faster                                                    |
| deltablue                  | 2.75 ms                                                | 2.53 ms: 1.09x faster                                                   |
| raytrace                   | 206 ms                                                 | 190 ms: 1.08x faster                                                    |
| async_tree_io_tg           | 724 ms                                                 | 673 ms: 1.08x faster                                                    |
| asyncio_tcp_ssl            | 1.40 sec                                               | 1.31 sec: 1.07x faster                                                  |
| generators                 | 30.3 ms                                                | 28.5 ms: 1.06x faster                                                   |
| async_tree_none_tg         | 276 ms                                                 | 261 ms: 1.06x faster                                                    |
| sqlglot_transpile          | 1.05 ms                                                | 1.00 ms: 1.05x faster                                                   |
| sympy_sum                  | 80.2 ms                                                | 77.5 ms: 1.04x faster                                                   |
| async_tree_cpu_io_mixed_tg | 550 ms                                                 | 533 ms: 1.03x faster                                                    |
| richards_super             | 37.3 ms                                                | 37.1 ms: 1.01x faster                                                   |
| crypto_pyaes               | 47.5 ms                                                | 47.4 ms: 1.00x faster                                                   |
| sympy_str                  | 144 ms                                                 | 144 ms: 1.00x slower                                                    |
| create_gc_cycles           | 711 us                                                 | 714 us: 1.01x slower                                                    |
| pidigits                   | 280 ms                                                 | 282 ms: 1.01x slower                                                    |
| async_tree_cpu_io_mixed    | 519 ms                                                 | 523 ms: 1.01x slower                                                    |
| unpickle_pure_python       | 149 us                                                 | 150 us: 1.01x slower                                                    |
| logging_simple             | 3.41 us                                                | 3.45 us: 1.01x slower                                                   |
| gc_traversal               | 2.38 ms                                                | 2.41 ms: 1.01x slower                                                   |
| sympy_integrate            | 11.3 ms                                                | 11.4 ms: 1.01x slower                                                   |
| async_tree_io              | 697 ms                                                 | 706 ms: 1.01x slower                                                    |
| deepcopy_memo              | 25.7 us                                                | 26.2 us: 1.02x slower                                                   |
| logging_format             | 3.67 us                                                | 3.76 us: 1.02x slower                                                   |
| scimark_monte_carlo        | 43.5 ms                                                | 44.9 ms: 1.03x slower                                                   |
| regex_dna                  | 148 ms                                                 | 153 ms: 1.03x slower                                                    |
| pickle_pure_python         | 191 us                                                 | 198 us: 1.03x slower                                                    |
| dask                       | 219 ms                                                 | 227 ms: 1.04x slower                                                    |
| pickle                     | 6.98 us                                                | 7.24 us: 1.04x slower                                                   |
| go                         | 105 ms                                                 | 110 ms: 1.04x slower                                                    |
| float                      | 50.8 ms                                                | 53.0 ms: 1.04x slower                                                   |
| tomli_loads                | 1.27 sec                                               | 1.33 sec: 1.05x slower                                                  |
| meteor_contest             | 71.1 ms                                                | 74.7 ms: 1.05x slower                                                   |
| pprint_safe_repr           | 478 ms                                                 | 504 ms: 1.05x slower                                                    |
| xml_etree_parse            | 100 ms                                                 | 106 ms: 1.06x slower                                                    |
| pprint_pformat             | 979 ms                                                 | 1.04 sec: 1.06x slower                                                  |
| deepcopy                   | 215 us                                                 | 229 us: 1.06x slower                                                    |
| pickle_dict                | 17.1 us                                                | 18.1 us: 1.06x slower                                                   |
| docutils                   | 1.43 sec                                               | 1.52 sec: 1.07x slower                                                  |
| coroutines                 | 17.2 ms                                                | 18.3 ms: 1.07x slower                                                   |
| dulwich_log                | 28.6 ms                                                | 30.6 ms: 1.07x slower                                                   |
| fannkuch                   | 240 ms                                                 | 256 ms: 1.07x slower                                                    |
| richards                   | 31.1 ms                                                | 33.3 ms: 1.07x slower                                                   |
| gunicorn                   | 1.10 ms                                                | 1.18 ms: 1.08x slower                                                   |
| json                       | 2.75 ms                                                | 2.96 ms: 1.08x slower                                                   |
| html5lib                   | 33.0 ms                                                | 35.6 ms: 1.08x slower                                                   |
| pathlib                    | 23.2 ms                                                | 25.1 ms: 1.08x slower                                                   |
| regex_effbot               | 2.43 ms                                                | 2.63 ms: 1.08x slower                                                   |
| sympy_expand               | 229 ms                                                 | 248 ms: 1.08x slower                                                    |
| mdp                        | 1.48 sec                                               | 1.61 sec: 1.08x slower                                                  |
| logging_silent             | 66.5 ns                                                | 72.2 ns: 1.08x slower                                                   |
| hexiom                     | 4.58 ms                                                | 4.97 ms: 1.09x slower                                                   |
| django_template            | 20.1 ms                                                | 21.9 ms: 1.09x slower                                                   |
| genshi_text                | 14.4 ms                                                | 15.7 ms: 1.09x slower                                                   |
| pycparser                  | 659 ms                                                 | 717 ms: 1.09x slower                                                    |
| aiohttp                    | 1.02 ms                                                | 1.12 ms: 1.09x slower                                                   |
| xml_etree_iterparse        | 68.3 ms                                                | 74.9 ms: 1.10x slower                                                   |
| deepcopy_reduce            | 1.79 us                                                | 1.97 us: 1.10x slower                                                   |
| bench_thread_pool          | 465 us                                                 | 513 us: 1.10x slower                                                    |
| unpickle                   | 8.29 us                                                | 9.18 us: 1.11x slower                                                   |
| pickle_list                | 2.70 us                                                | 2.99 us: 1.11x slower                                                   |
| scimark_sparse_mat_mult    | 2.81 ms                                                | 3.13 ms: 1.11x slower                                                   |
| coverage                   | 43.9 ms                                                | 48.9 ms: 1.11x slower                                                   |
| json_loads                 | 15.3 us                                                | 17.1 us: 1.11x slower                                                   |
| chameleon                  | 4.30 ms                                                | 4.84 ms: 1.13x slower                                                   |
| thrift                     | 410 us                                                 | 463 us: 1.13x slower                                                    |
| sqlglot_normalize          | 162 ms                                                 | 183 ms: 1.13x slower                                                    |
| spectral_norm              | 65.7 ms                                                | 74.7 ms: 1.14x slower                                                   |
| regex_v8                   | 15.1 ms                                                | 17.3 ms: 1.14x slower                                                   |
| nqueens                    | 55.9 ms                                                | 63.8 ms: 1.14x slower                                                   |
| nbody                      | 61.7 ms                                                | 70.4 ms: 1.14x slower                                                   |
| scimark_fft                | 173 ms                                                 | 199 ms: 1.15x slower                                                    |
| xml_etree_process          | 33.6 ms                                                | 38.8 ms: 1.16x slower                                                   |
| unpickle_list              | 2.69 us                                                | 3.11 us: 1.16x slower                                                   |
| pyflate                    | 284 ms                                                 | 331 ms: 1.17x slower                                                    |
| regex_compile              | 72.8 ms                                                | 85.2 ms: 1.17x slower                                                   |
| sqlglot_optimize           | 29.6 ms                                                | 35.0 ms: 1.18x slower                                                   |
| 2to3                       | 154 ms                                                 | 183 ms: 1.18x slower                                                    |
| genshi_xml                 | 28.5 ms                                                | 34.2 ms: 1.20x slower                                                   |
| tornado_http               | 69.1 ms                                                | 83.7 ms: 1.21x slower                                                   |
| xml_etree_generate         | 45.8 ms                                                | 55.8 ms: 1.22x slower                                                   |
| bench_mp_pool              | 41.0 ms                                                | 51.3 ms: 1.25x slower                                                   |
| scimark_lu                 | 67.7 ms                                                | 84.9 ms: 1.25x slower                                                   |
| sqlite_synth               | 1.26 us                                                | 1.59 us: 1.27x slower                                                   |
| scimark_sor                | 79.2 ms                                                | 111 ms: 1.40x slower                                                    |
| telco                      | 3.17 ms                                                | 4.49 ms: 1.42x slower                                                   |
| python_startup             | 10.8 ms                                                | 16.8 ms: 1.56x slower                                                   |
| async_generators           | 192 ms                                                 | 311 ms: 1.62x slower                                                    |
| mypy2                      | 372 ms                                                 | 619 ms: 1.66x slower                                                    |
| python_startup_no_site     | 8.57 ms                                                | 15.2 ms: 1.77x slower                                                   |
| unpack_sequence            | 33.6 ns                                                | 114 ns: 3.38x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.06x slower                                                            |

Benchmark hidden because not significant (2): async_tree_memoization, asyncio_websockets
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (8) of results/bm-20240315-3.13.0a5+-e6d8e6d-JIT/bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5+-e6d8e6d.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x


# Memory

- memory change: 1.48x