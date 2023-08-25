
# Results vs. 3.11.0

- fork: brandtbucher
- ref: fold_slices_more
- machine: linux-x86_64
- commit hash: 97543c5
- commit date: 2023-04-06
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 250 ms: 1.03x faster                                                     |
| chameleon      | 6.47 ms                                                | 6.41 ms: 1.01x faster                                                    |
| docutils       | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                   |
| html5lib       | 64.5 ms                                                | 61.0 ms: 1.06x faster                                                    |
| tornado_http   | 96.3 ms                                                | 90.6 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                  | 1.04x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 86.9 ms: 1.07x faster                                                    |
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                                     |
| float          | 77.2 ms                                                | 74.7 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                  | 1.05x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.41 ms: 1.17x faster                                                    |
| regex_compile  | 138 ms                                                 | 132 ms: 1.05x faster                                                     |
| regex_v8       | 22.0 ms                                                | 21.6 ms: 1.02x faster                                                    |
| regex_dna      | 204 ms                                                 | 204 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                  | 1.06x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.37 ms: 1.34x faster                                                    |
| unpickle_pure_python | 228 us                                                 | 202 us: 1.13x faster                                                     |
| json_loads           | 26.5 us                                                | 24.2 us: 1.10x faster                                                    |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.07x faster                                                     |
| pickle_pure_python   | 306 us                                                 | 287 us: 1.07x faster                                                     |
| xml_etree_iterparse  | 104 ms                                                 | 99.4 ms: 1.05x faster                                                    |
| pickle_dict          | 31.1 us                                                | 31.9 us: 1.02x slower                                                    |
| xml_etree_process    | 53.9 ms                                                | 55.3 ms: 1.03x slower                                                    |
| unpickle_list        | 4.91 us                                                | 5.05 us: 1.03x slower                                                    |
| pickle               | 10.1 us                                                | 10.6 us: 1.05x slower                                                    |
| xml_etree_generate   | 76.2 ms                                                | 80.6 ms: 1.06x slower                                                    |
| pickle_list          | 4.11 us                                                | 4.43 us: 1.08x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.82 ms: 1.03x slower                                                    |
| python_startup_no_site | 6.01 ms                                                | 6.52 ms: 1.09x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 46.9 ms: 1.10x faster                                                    |
| genshi_text     | 21.6 ms                                                | 21.1 ms: 1.02x faster                                                    |
| django_template | 32.6 ms                                                | 32.4 ms: 1.00x faster                                                    |
| mako            | 10.1 ms                                                | 10.1 ms: 1.00x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.9 ms: 2.46x faster                                                    |
| asyncio_tcp             | 922 ms                                                 | 500 ms: 1.84x faster                                                     |
| json_dumps              | 12.6 ms                                                | 9.37 ms: 1.34x faster                                                    |
| mypy2                   | 420 ms                                                 | 334 ms: 1.26x faster                                                     |
| regex_effbot            | 3.99 ms                                                | 3.41 ms: 1.17x faster                                                    |
| sqlglot_parse           | 1.40 ms                                                | 1.22 ms: 1.14x faster                                                    |
| sqlglot_transpile       | 1.70 ms                                                | 1.50 ms: 1.14x faster                                                    |
| deltablue               | 3.67 ms                                                | 3.24 ms: 1.13x faster                                                    |
| unpickle_pure_python    | 228 us                                                 | 202 us: 1.13x faster                                                     |
| richards                | 45.7 ms                                                | 41.4 ms: 1.10x faster                                                    |
| genshi_xml              | 51.8 ms                                                | 46.9 ms: 1.10x faster                                                    |
| json_loads              | 26.5 us                                                | 24.2 us: 1.10x faster                                                    |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                    |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                                    |
| deepcopy_memo           | 37.0 us                                                | 34.3 us: 1.08x faster                                                    |
| hexiom                  | 6.37 ms                                                | 5.92 ms: 1.08x faster                                                    |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.07x faster                                                     |
| coroutines              | 25.5 ms                                                | 23.7 ms: 1.07x faster                                                    |
| nbody                   | 93.1 ms                                                | 86.9 ms: 1.07x faster                                                    |
| json                    | 4.94 ms                                                | 4.63 ms: 1.07x faster                                                    |
| pickle_pure_python      | 306 us                                                 | 287 us: 1.07x faster                                                     |
| logging_silent          | 101 ns                                                 | 95.0 ns: 1.06x faster                                                    |
| tornado_http            | 96.3 ms                                                | 90.6 ms: 1.06x faster                                                    |
| logging_format          | 6.68 us                                                | 6.30 us: 1.06x faster                                                    |
| html5lib                | 64.5 ms                                                | 61.0 ms: 1.06x faster                                                    |
| chaos                   | 69.2 ms                                                | 65.4 ms: 1.06x faster                                                    |
| logging_simple          | 6.03 us                                                | 5.71 us: 1.06x faster                                                    |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.27 ms: 1.05x faster                                                    |
| sqlglot_optimize        | 53.1 ms                                                | 50.4 ms: 1.05x faster                                                    |
| spectral_norm           | 100 ms                                                 | 95.1 ms: 1.05x faster                                                    |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                                     |
| deepcopy                | 342 us                                                 | 326 us: 1.05x faster                                                     |
| raytrace                | 297 ms                                                 | 283 ms: 1.05x faster                                                     |
| scimark_sor             | 118 ms                                                 | 113 ms: 1.05x faster                                                     |
| regex_compile           | 138 ms                                                 | 132 ms: 1.05x faster                                                     |
| scimark_fft             | 328 ms                                                 | 314 ms: 1.05x faster                                                     |
| xml_etree_iterparse     | 104 ms                                                 | 99.4 ms: 1.05x faster                                                    |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.04x faster                                                     |
| coverage                | 100 ms                                                 | 96.3 ms: 1.04x faster                                                    |
| docutils                | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                   |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                     |
| bench_thread_pool       | 819 us                                                 | 791 us: 1.04x faster                                                     |
| mdp                     | 2.62 sec                                               | 2.53 sec: 1.03x faster                                                   |
| float                   | 77.2 ms                                                | 74.7 ms: 1.03x faster                                                    |
| 2to3                    | 259 ms                                                 | 250 ms: 1.03x faster                                                     |
| sympy_expand            | 475 ms                                                 | 460 ms: 1.03x faster                                                     |
| pycparser               | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                   |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                                    |
| pprint_pformat          | 1.46 sec                                               | 1.42 sec: 1.03x faster                                                   |
| comprehensions          | 22.4 us                                                | 21.9 us: 1.02x faster                                                    |
| sympy_str               | 290 ms                                                 | 284 ms: 1.02x faster                                                     |
| genshi_text             | 21.6 ms                                                | 21.1 ms: 1.02x faster                                                    |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.02x faster                                                     |
| regex_v8                | 22.0 ms                                                | 21.6 ms: 1.02x faster                                                    |
| sqlalchemy_imperative   | 17.9 ms                                                | 17.6 ms: 1.02x faster                                                    |
| telco                   | 6.58 ms                                                | 6.47 ms: 1.02x faster                                                    |
| gc_traversal            | 4.02 ms                                                | 3.97 ms: 1.01x faster                                                    |
| go                      | 140 ms                                                 | 138 ms: 1.01x faster                                                     |
| fannkuch                | 388 ms                                                 | 383 ms: 1.01x faster                                                     |
| pprint_safe_repr        | 701 ms                                                 | 694 ms: 1.01x faster                                                     |
| crypto_pyaes            | 74.7 ms                                                | 73.9 ms: 1.01x faster                                                    |
| nqueens                 | 83.4 ms                                                | 82.6 ms: 1.01x faster                                                    |
| dulwich_log             | 63.7 ms                                                | 63.1 ms: 1.01x faster                                                    |
| chameleon               | 6.47 ms                                                | 6.41 ms: 1.01x faster                                                    |
| sympy_sum               | 167 ms                                                 | 165 ms: 1.01x faster                                                     |
| scimark_lu              | 110 ms                                                 | 109 ms: 1.01x faster                                                     |
| deepcopy_reduce         | 2.94 us                                                | 2.92 us: 1.01x faster                                                    |
| pathlib                 | 18.2 ms                                                | 18.1 ms: 1.01x faster                                                    |
| django_template         | 32.6 ms                                                | 32.4 ms: 1.00x faster                                                    |
| mako                    | 10.1 ms                                                | 10.1 ms: 1.00x faster                                                    |
| regex_dna               | 204 ms                                                 | 204 ms: 1.00x slower                                                     |
| unpack_sequence         | 43.1 ns                                                | 43.5 ns: 1.01x slower                                                    |
| pyflate                 | 418 ms                                                 | 425 ms: 1.02x slower                                                     |
| pickle_dict             | 31.1 us                                                | 31.9 us: 1.02x slower                                                    |
| create_gc_cycles        | 1.49 ms                                                | 1.52 ms: 1.03x slower                                                    |
| xml_etree_process       | 53.9 ms                                                | 55.3 ms: 1.03x slower                                                    |
| unpickle_list           | 4.91 us                                                | 5.05 us: 1.03x slower                                                    |
| thrift                  | 756 us                                                 | 782 us: 1.03x slower                                                     |
| python_startup          | 8.52 ms                                                | 8.82 ms: 1.03x slower                                                    |
| sqlite_synth            | 2.52 us                                                | 2.64 us: 1.05x slower                                                    |
| pickle                  | 10.1 us                                                | 10.6 us: 1.05x slower                                                    |
| xml_etree_generate      | 76.2 ms                                                | 80.6 ms: 1.06x slower                                                    |
| pickle_list             | 4.11 us                                                | 4.43 us: 1.08x slower                                                    |
| python_startup_no_site  | 6.01 ms                                                | 6.52 ms: 1.09x slower                                                    |
| async_generators        | 368 ms                                                 | 413 ms: 1.12x slower                                                     |
| dask                    | 360 ms                                                 | 503 ms: 1.40x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                             |

Benchmark hidden because not significant (8): djangocms, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization, async_tree_io, bench_mp_pool, scimark_monte_carlo, unpickle
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
