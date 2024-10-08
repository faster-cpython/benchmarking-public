# Results vs. base

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 1e7db3e
- commit date: 2024-07-29
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 273 ms                                                                | 289 ms: 1.06x slower                                                      |
| docutils       | 2.91 sec                                                              | 3.09 sec: 1.06x slower                                                    |
| html5lib       | 66.2 ms                                                               | 67.5 ms: 1.02x slower                                                     |
| tornado_http   | 92.3 ms                                                               | 94.7 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| coroutines             | 22.9 ms                                                               | 22.4 ms: 1.02x faster                                                     |
| asyncio_websockets     | 559 ms                                                                | 555 ms: 1.01x faster                                                      |
| asyncio_tcp            | 505 ms                                                                | 507 ms: 1.00x slower                                                      |
| async_tree_memoization | 418 ms                                                                | 429 ms: 1.03x slower                                                      |
| async_generators       | 453 ms                                                                | 473 ms: 1.04x slower                                                      |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (8): asyncio_tcp_ssl, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                | 186 ms: 1.00x slower                                                      |
| float          | 71.0 ms                                                               | 71.6 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.81 ms                                                               | 3.70 ms: 1.03x faster                                                     |
| regex_v8       | 24.5 ms                                                               | 24.2 ms: 1.01x faster                                                     |
| regex_dna      | 226 ms                                                                | 225 ms: 1.01x faster                                                      |
| regex_compile  | 134 ms                                                                | 151 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 10.3 ms                                                               | 10.2 ms: 1.01x faster                                                     |
| json_loads           | 27.7 us                                                               | 27.9 us: 1.01x slower                                                     |
| xml_etree_iterparse  | 99.6 ms                                                               | 101 ms: 1.01x slower                                                      |
| unpickle_pure_python | 213 us                                                                | 216 us: 1.02x slower                                                      |
| pickle_pure_python   | 299 us                                                                | 304 us: 1.02x slower                                                      |
| xml_etree_process    | 56.4 ms                                                               | 57.9 ms: 1.03x slower                                                     |
| xml_etree_generate   | 79.7 ms                                                               | 82.0 ms: 1.03x slower                                                     |
| tomli_loads          | 1.92 sec                                                              | 1.98 sec: 1.03x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                     |
| python_startup_no_site | 7.11 ms                                                               | 7.13 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                               | 9.63 ms: 1.02x faster                                                     |
| genshi_text     | 24.1 ms                                                               | 24.6 ms: 1.02x slower                                                     |
| genshi_xml      | 53.8 ms                                                               | 56.2 ms: 1.04x slower                                                     |
| django_template | 36.1 ms                                                               | 38.0 ms: 1.05x slower                                                     |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                              |

All benchmarks:
===============

| Benchmark                | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deltablue                | 3.52 ms                                                               | 3.08 ms: 1.14x faster                                                     |
| deepcopy_memo            | 29.0 us                                                               | 27.9 us: 1.04x faster                                                     |
| logging_silent           | 104 ns                                                                | 101 ns: 1.03x faster                                                      |
| regex_effbot             | 3.81 ms                                                               | 3.70 ms: 1.03x faster                                                     |
| deepcopy_reduce          | 2.72 us                                                               | 2.66 us: 1.02x faster                                                     |
| spectral_norm            | 105 ms                                                                | 102 ms: 1.02x faster                                                      |
| coroutines               | 22.9 ms                                                               | 22.4 ms: 1.02x faster                                                     |
| mako                     | 9.81 ms                                                               | 9.63 ms: 1.02x faster                                                     |
| json_dumps               | 10.3 ms                                                               | 10.2 ms: 1.01x faster                                                     |
| deepcopy                 | 274 us                                                                | 271 us: 1.01x faster                                                      |
| regex_v8                 | 24.5 ms                                                               | 24.2 ms: 1.01x faster                                                     |
| regex_dna                | 226 ms                                                                | 225 ms: 1.01x faster                                                      |
| asyncio_websockets       | 559 ms                                                                | 555 ms: 1.01x faster                                                      |
| thrift                   | 797 us                                                                | 792 us: 1.01x faster                                                      |
| crypto_pyaes             | 67.3 ms                                                               | 67.0 ms: 1.01x faster                                                     |
| pidigits                 | 186 ms                                                                | 186 ms: 1.00x slower                                                      |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                     |
| scimark_sparse_mat_mult  | 4.40 ms                                                               | 4.42 ms: 1.00x slower                                                     |
| python_startup_no_site   | 7.11 ms                                                               | 7.13 ms: 1.00x slower                                                     |
| asyncio_tcp              | 505 ms                                                                | 507 ms: 1.00x slower                                                      |
| json_loads               | 27.7 us                                                               | 27.9 us: 1.01x slower                                                     |
| logging_format           | 6.07 us                                                               | 6.12 us: 1.01x slower                                                     |
| float                    | 71.0 ms                                                               | 71.6 ms: 1.01x slower                                                     |
| xml_etree_iterparse      | 99.6 ms                                                               | 101 ms: 1.01x slower                                                      |
| scimark_fft              | 309 ms                                                                | 313 ms: 1.01x slower                                                      |
| dask                     | 363 ms                                                                | 368 ms: 1.01x slower                                                      |
| create_gc_cycles         | 1.74 ms                                                               | 1.76 ms: 1.01x slower                                                     |
| logging_simple           | 5.47 us                                                               | 5.57 us: 1.02x slower                                                     |
| bpe_tokeniser            | 4.52 sec                                                              | 4.60 sec: 1.02x slower                                                    |
| pathlib                  | 16.1 ms                                                               | 16.4 ms: 1.02x slower                                                     |
| unpickle_pure_python     | 213 us                                                                | 216 us: 1.02x slower                                                      |
| pickle_pure_python       | 299 us                                                                | 304 us: 1.02x slower                                                      |
| meteor_contest           | 105 ms                                                                | 107 ms: 1.02x slower                                                      |
| telco                    | 7.82 ms                                                               | 7.98 ms: 1.02x slower                                                     |
| html5lib                 | 66.2 ms                                                               | 67.5 ms: 1.02x slower                                                     |
| genshi_text              | 24.1 ms                                                               | 24.6 ms: 1.02x slower                                                     |
| mdp                      | 2.56 sec                                                              | 2.62 sec: 1.02x slower                                                    |
| tornado_http             | 92.3 ms                                                               | 94.7 ms: 1.03x slower                                                     |
| async_tree_memoization   | 418 ms                                                                | 429 ms: 1.03x slower                                                      |
| xml_etree_process        | 56.4 ms                                                               | 57.9 ms: 1.03x slower                                                     |
| xml_etree_generate       | 79.7 ms                                                               | 82.0 ms: 1.03x slower                                                     |
| tomli_loads              | 1.92 sec                                                              | 1.98 sec: 1.03x slower                                                    |
| bench_thread_pool        | 815 us                                                                | 839 us: 1.03x slower                                                      |
| pprint_safe_repr         | 734 ms                                                                | 757 ms: 1.03x slower                                                      |
| fannkuch                 | 363 ms                                                                | 375 ms: 1.03x slower                                                      |
| scimark_sor              | 129 ms                                                                | 134 ms: 1.04x slower                                                      |
| sqlglot_parse            | 1.30 ms                                                               | 1.34 ms: 1.04x slower                                                     |
| typing_runtime_protocols | 170 us                                                                | 176 us: 1.04x slower                                                      |
| pycparser                | 1.16 sec                                                              | 1.20 sec: 1.04x slower                                                    |
| chaos                    | 57.8 ms                                                               | 60.0 ms: 1.04x slower                                                     |
| generators               | 32.7 ms                                                               | 34.1 ms: 1.04x slower                                                     |
| pyflate                  | 431 ms                                                                | 450 ms: 1.04x slower                                                      |
| async_generators         | 453 ms                                                                | 473 ms: 1.04x slower                                                      |
| genshi_xml               | 53.8 ms                                                               | 56.2 ms: 1.04x slower                                                     |
| pprint_pformat           | 1.49 sec                                                              | 1.56 sec: 1.04x slower                                                    |
| scimark_monte_carlo      | 60.9 ms                                                               | 63.7 ms: 1.05x slower                                                     |
| go                       | 145 ms                                                                | 152 ms: 1.05x slower                                                      |
| sqlglot_transpile        | 1.63 ms                                                               | 1.71 ms: 1.05x slower                                                     |
| django_template          | 36.1 ms                                                               | 38.0 ms: 1.05x slower                                                     |
| comprehensions           | 16.1 us                                                               | 17.0 us: 1.05x slower                                                     |
| 2to3                     | 273 ms                                                                | 289 ms: 1.06x slower                                                      |
| raytrace                 | 266 ms                                                                | 281 ms: 1.06x slower                                                      |
| docutils                 | 2.91 sec                                                              | 3.09 sec: 1.06x slower                                                    |
| scimark_lu               | 124 ms                                                                | 132 ms: 1.06x slower                                                      |
| sqlglot_normalize        | 111 ms                                                                | 119 ms: 1.06x slower                                                      |
| sympy_expand             | 507 ms                                                                | 545 ms: 1.07x slower                                                      |
| sympy_str                | 298 ms                                                                | 322 ms: 1.08x slower                                                      |
| sqlglot_optimize         | 55.9 ms                                                               | 60.4 ms: 1.08x slower                                                     |
| gc_traversal             | 3.52 ms                                                               | 3.81 ms: 1.08x slower                                                     |
| sympy_sum                | 170 ms                                                                | 186 ms: 1.09x slower                                                      |
| richards                 | 40.5 ms                                                               | 44.7 ms: 1.10x slower                                                     |
| richards_super           | 46.4 ms                                                               | 51.3 ms: 1.11x slower                                                     |
| sympy_integrate          | 22.4 ms                                                               | 24.8 ms: 1.11x slower                                                     |
| pylint                   | 355 ms                                                                | 394 ms: 1.11x slower                                                      |
| nqueens                  | 84.5 ms                                                               | 94.6 ms: 1.12x slower                                                     |
| regex_compile            | 134 ms                                                                | 151 ms: 1.13x slower                                                      |
| hexiom                   | 6.68 ms                                                               | 8.07 ms: 1.21x slower                                                     |
| Geometric mean           | (ref)                                                                 | 1.03x slower                                                              |

Benchmark hidden because not significant (13): xml_etree_parse, coverage, bench_mp_pool, asyncio_tcp_ssl, async_tree_none_tg, json, nbody, async_tree_memoization_tg, async_tree_io_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.02x