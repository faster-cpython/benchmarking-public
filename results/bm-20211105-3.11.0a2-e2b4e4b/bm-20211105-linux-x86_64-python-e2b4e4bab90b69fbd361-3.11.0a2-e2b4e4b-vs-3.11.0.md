
# Results vs. 3.11.0

- fork: python
- ref: e2b4e4bab90b69fbd361
- machine: linux-x86_64
- commit hash: e2b4e4b
- commit date: 2021-11-05
- overall geometric mean: 1.08x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 274 ms: 1.06x slower                                                  |
| chameleon      | 6.47 ms                                                | 7.46 ms: 1.15x slower                                                 |
| docutils       | 2.63 sec                                               | 2.79 sec: 1.06x slower                                                |
| html5lib       | 64.5 ms                                                | 71.5 ms: 1.11x slower                                                 |
| tornado_http   | 96.3 ms                                                | 111 ms: 1.15x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 188 ms: 1.06x faster                                                  |
| float          | 77.2 ms                                                | 83.3 ms: 1.08x slower                                                 |
| nbody          | 93.1 ms                                                | 112 ms: 1.20x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.26 ms: 1.23x faster                                                 |
| regex_compile  | 138 ms                                                 | 145 ms: 1.05x slower                                                  |
| regex_dna      | 204 ms                                                 | 219 ms: 1.07x slower                                                  |
| regex_v8       | 22.0 ms                                                | 23.7 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_dict          | 31.1 us                                                | 28.6 us: 1.09x faster                                                 |
| json_loads           | 26.5 us                                                | 25.9 us: 1.02x faster                                                 |
| json_dumps           | 12.6 ms                                                | 12.4 ms: 1.02x faster                                                 |
| unpickle_list        | 4.91 us                                                | 5.13 us: 1.05x slower                                                 |
| xml_etree_iterparse  | 104 ms                                                 | 110 ms: 1.06x slower                                                  |
| xml_etree_generate   | 76.2 ms                                                | 81.6 ms: 1.07x slower                                                 |
| xml_etree_process    | 53.9 ms                                                | 59.6 ms: 1.11x slower                                                 |
| pickle_list          | 4.11 us                                                | 4.68 us: 1.14x slower                                                 |
| unpickle_pure_python | 228 us                                                 | 271 us: 1.19x slower                                                  |
| pickle_pure_python   | 306 us                                                 | 364 us: 1.19x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x slower                                                          |

Benchmark hidden because not significant (3): xml_etree_parse, pickle, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.01 ms                                                | 5.77 ms: 1.04x faster                                                 |
| python_startup         | 8.52 ms                                                | 14.6 ms: 1.71x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 56.1 ms: 1.08x slower                                                 |
| genshi_text     | 21.6 ms                                                | 24.6 ms: 1.14x slower                                                 |
| django_template | 32.6 ms                                                | 37.9 ms: 1.16x slower                                                 |
| mako            | 10.1 ms                                                | 12.1 ms: 1.20x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.15x slower                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coverage                | 100 ms                                                 | 75.8 ms: 1.32x faster                                                 |
| generators              | 73.5 ms                                                | 57.4 ms: 1.28x faster                                                 |
| regex_effbot            | 3.99 ms                                                | 3.26 ms: 1.23x faster                                                 |
| pickle_dict             | 31.1 us                                                | 28.6 us: 1.09x faster                                                 |
| pidigits                | 198 ms                                                 | 188 ms: 1.06x faster                                                  |
| python_startup_no_site  | 6.01 ms                                                | 5.77 ms: 1.04x faster                                                 |
| async_generators        | 368 ms                                                 | 361 ms: 1.02x faster                                                  |
| gunicorn                | 1.18 ms                                                | 1.15 ms: 1.02x faster                                                 |
| json_loads              | 26.5 us                                                | 25.9 us: 1.02x faster                                                 |
| async_tree_none         | 526 ms                                                 | 518 ms: 1.02x faster                                                  |
| json_dumps              | 12.6 ms                                                | 12.4 ms: 1.02x faster                                                 |
| telco                   | 6.58 ms                                                | 6.50 ms: 1.01x faster                                                 |
| logging_simple          | 6.03 us                                                | 6.07 us: 1.01x slower                                                 |
| unpack_sequence         | 43.1 ns                                                | 43.6 ns: 1.01x slower                                                 |
| sympy_sum               | 167 ms                                                 | 170 ms: 1.02x slower                                                  |
| mdp                     | 2.62 sec                                               | 2.71 sec: 1.04x slower                                                |
| unpickle_list           | 4.91 us                                                | 5.13 us: 1.05x slower                                                 |
| regex_compile           | 138 ms                                                 | 145 ms: 1.05x slower                                                  |
| sqlalchemy_imperative   | 17.9 ms                                                | 18.8 ms: 1.05x slower                                                 |
| flaskblogging           | 7.12 ms                                                | 7.46 ms: 1.05x slower                                                 |
| pathlib                 | 18.2 ms                                                | 19.1 ms: 1.05x slower                                                 |
| sqlalchemy_declarative  | 138 ms                                                 | 145 ms: 1.05x slower                                                  |
| sympy_str               | 290 ms                                                 | 306 ms: 1.06x slower                                                  |
| spectral_norm           | 100 ms                                                 | 106 ms: 1.06x slower                                                  |
| 2to3                    | 259 ms                                                 | 274 ms: 1.06x slower                                                  |
| sympy_integrate         | 21.0 ms                                                | 22.2 ms: 1.06x slower                                                 |
| docutils                | 2.63 sec                                               | 2.79 sec: 1.06x slower                                                |
| sympy_expand            | 475 ms                                                 | 505 ms: 1.06x slower                                                  |
| xml_etree_iterparse     | 104 ms                                                 | 110 ms: 1.06x slower                                                  |
| pycparser               | 1.18 sec                                               | 1.26 sec: 1.06x slower                                                |
| xml_etree_generate      | 76.2 ms                                                | 81.6 ms: 1.07x slower                                                 |
| regex_dna               | 204 ms                                                 | 219 ms: 1.07x slower                                                  |
| dulwich_log             | 63.7 ms                                                | 68.3 ms: 1.07x slower                                                 |
| regex_v8                | 22.0 ms                                                | 23.7 ms: 1.08x slower                                                 |
| async_tree_memoization  | 627 ms                                                 | 676 ms: 1.08x slower                                                  |
| float                   | 77.2 ms                                                | 83.3 ms: 1.08x slower                                                 |
| scimark_fft             | 328 ms                                                 | 355 ms: 1.08x slower                                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.86 ms: 1.08x slower                                                 |
| genshi_xml              | 51.8 ms                                                | 56.1 ms: 1.08x slower                                                 |
| pprint_pformat          | 1.46 sec                                               | 1.58 sec: 1.08x slower                                                |
| thrift                  | 756 us                                                 | 821 us: 1.09x slower                                                  |
| async_tree_io           | 1.30 sec                                               | 1.41 sec: 1.09x slower                                                |
| pprint_safe_repr        | 701 ms                                                 | 763 ms: 1.09x slower                                                  |
| bench_thread_pool       | 819 us                                                 | 892 us: 1.09x slower                                                  |
| deepcopy_memo           | 37.0 us                                                | 40.4 us: 1.09x slower                                                 |
| sqlite_synth            | 2.52 us                                                | 2.76 us: 1.09x slower                                                 |
| nqueens                 | 83.4 ms                                                | 91.4 ms: 1.10x slower                                                 |
| sqlglot_optimize        | 53.1 ms                                                | 58.4 ms: 1.10x slower                                                 |
| raytrace                | 297 ms                                                 | 326 ms: 1.10x slower                                                  |
| fannkuch                | 388 ms                                                 | 427 ms: 1.10x slower                                                  |
| xml_etree_process       | 53.9 ms                                                | 59.6 ms: 1.11x slower                                                 |
| async_tree_cpu_io_mixed | 739 ms                                                 | 818 ms: 1.11x slower                                                  |
| html5lib                | 64.5 ms                                                | 71.5 ms: 1.11x slower                                                 |
| sqlglot_normalize       | 108 ms                                                 | 119 ms: 1.11x slower                                                  |
| chaos                   | 69.2 ms                                                | 77.1 ms: 1.11x slower                                                 |
| deepcopy_reduce         | 2.94 us                                                | 3.27 us: 1.11x slower                                                 |
| deepcopy                | 342 us                                                 | 382 us: 1.12x slower                                                  |
| coroutines              | 25.5 ms                                                | 28.8 ms: 1.13x slower                                                 |
| pickle_list             | 4.11 us                                                | 4.68 us: 1.14x slower                                                 |
| genshi_text             | 21.6 ms                                                | 24.6 ms: 1.14x slower                                                 |
| tornado_http            | 96.3 ms                                                | 111 ms: 1.15x slower                                                  |
| scimark_monte_carlo     | 68.1 ms                                                | 78.4 ms: 1.15x slower                                                 |
| chameleon               | 6.47 ms                                                | 7.46 ms: 1.15x slower                                                 |
| logging_silent          | 101 ns                                                 | 117 ns: 1.15x slower                                                  |
| django_template         | 32.6 ms                                                | 37.9 ms: 1.16x slower                                                 |
| hexiom                  | 6.37 ms                                                | 7.42 ms: 1.16x slower                                                 |
| unpickle_pure_python    | 228 us                                                 | 271 us: 1.19x slower                                                  |
| pickle_pure_python      | 306 us                                                 | 364 us: 1.19x slower                                                  |
| go                      | 140 ms                                                 | 167 ms: 1.20x slower                                                  |
| mako                    | 10.1 ms                                                | 12.1 ms: 1.20x slower                                                 |
| nbody                   | 93.1 ms                                                | 112 ms: 1.20x slower                                                  |
| crypto_pyaes            | 74.7 ms                                                | 90.2 ms: 1.21x slower                                                 |
| richards                | 45.7 ms                                                | 55.7 ms: 1.22x slower                                                 |
| scimark_lu              | 110 ms                                                 | 136 ms: 1.24x slower                                                  |
| pyflate                 | 418 ms                                                 | 541 ms: 1.29x slower                                                  |
| scimark_sor             | 118 ms                                                 | 156 ms: 1.32x slower                                                  |
| deltablue               | 3.67 ms                                                | 4.86 ms: 1.32x slower                                                 |
| sqlglot_transpile       | 1.70 ms                                                | 2.37 ms: 1.39x slower                                                 |
| sqlglot_parse           | 1.40 ms                                                | 2.06 ms: 1.47x slower                                                 |
| python_startup          | 8.52 ms                                                | 14.6 ms: 1.71x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.08x slower                                                          |

Benchmark hidden because not significant (8): json, xml_etree_parse, meteor_contest, pickle, bench_mp_pool, unpickle, logging_format, pylint
Ignored benchmarks (12) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, djangocms, gc_traversal, mypy2, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x
