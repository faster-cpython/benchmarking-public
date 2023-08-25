
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 4fe1c4b
- commit date: 2023-04-15
- overall geometric mean: 1.06x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-linux-x86_64-python-main-3.12.0a7+-4fe1c4b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 249 ms: 1.04x faster                                   |
| chameleon      | 6.47 ms                                                | 6.33 ms: 1.02x faster                                  |
| docutils       | 2.63 sec                                               | 2.51 sec: 1.05x faster                                 |
| html5lib       | 64.5 ms                                                | 60.7 ms: 1.06x faster                                  |
| tornado_http   | 96.3 ms                                                | 92.4 ms: 1.04x faster                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-linux-x86_64-python-main-3.12.0a7+-4fe1c4b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 85.1 ms: 1.09x faster                                  |
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                   |
| float          | 77.2 ms                                                | 73.5 ms: 1.05x faster                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-linux-x86_64-python-main-3.12.0a7+-4fe1c4b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.32 ms: 1.20x faster                                  |
| regex_compile  | 138 ms                                                 | 132 ms: 1.05x faster                                   |
| regex_v8       | 22.0 ms                                                | 21.3 ms: 1.03x faster                                  |
| regex_dna      | 204 ms                                                 | 202 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-linux-x86_64-python-main-3.12.0a7+-4fe1c4b |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.46 ms: 1.33x faster                                  |
| unpickle_pure_python | 228 us                                                 | 203 us: 1.12x faster                                   |
| json_loads           | 26.5 us                                                | 24.1 us: 1.10x faster                                  |
| pickle_pure_python   | 306 us                                                 | 285 us: 1.07x faster                                   |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                   |
| xml_etree_iterparse  | 104 ms                                                 | 99.3 ms: 1.05x faster                                  |
| unpickle_list        | 4.91 us                                                | 4.88 us: 1.01x faster                                  |
| xml_etree_process    | 53.9 ms                                                | 55.0 ms: 1.02x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 79.9 ms: 1.05x slower                                  |
| pickle_list          | 4.11 us                                                | 4.31 us: 1.05x slower                                  |
| pickle_dict          | 31.1 us                                                | 32.9 us: 1.06x slower                                  |
| unpickle             | 13.7 us                                                | 14.6 us: 1.07x slower                                  |
| pickle               | 10.1 us                                                | 10.9 us: 1.08x slower                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-linux-x86_64-python-main-3.12.0a7+-4fe1c4b |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.91 ms: 1.05x slower                                  |
| python_startup_no_site | 6.01 ms                                                | 6.60 ms: 1.10x slower                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-linux-x86_64-python-main-3.12.0a7+-4fe1c4b |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.1 ms: 1.10x faster                                  |
| genshi_text     | 21.6 ms                                                | 21.0 ms: 1.03x faster                                  |
| mako            | 10.1 ms                                                | 9.86 ms: 1.02x faster                                  |
| django_template | 32.6 ms                                                | 32.4 ms: 1.01x faster                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-linux-x86_64-python-main-3.12.0a7+-4fe1c4b |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 73.5 ms                                                | 28.0 ms: 2.62x faster                                  |
| asyncio_tcp             | 922 ms                                                 | 501 ms: 1.84x faster                                   |
| json_dumps              | 12.6 ms                                                | 9.46 ms: 1.33x faster                                  |
| mypy2                   | 420 ms                                                 | 331 ms: 1.27x faster                                   |
| regex_effbot            | 3.99 ms                                                | 3.32 ms: 1.20x faster                                  |
| coroutines              | 25.5 ms                                                | 21.5 ms: 1.19x faster                                  |
| sqlglot_parse           | 1.40 ms                                                | 1.19 ms: 1.17x faster                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.48 ms: 1.15x faster                                  |
| deltablue               | 3.67 ms                                                | 3.20 ms: 1.15x faster                                  |
| unpickle_pure_python    | 228 us                                                 | 203 us: 1.12x faster                                   |
| richards                | 45.7 ms                                                | 40.9 ms: 1.12x faster                                  |
| json_loads              | 26.5 us                                                | 24.1 us: 1.10x faster                                  |
| genshi_xml              | 51.8 ms                                                | 47.1 ms: 1.10x faster                                  |
| aiohttp                 | 1.10 ms                                                | 1.00 ms: 1.10x faster                                  |
| nbody                   | 93.1 ms                                                | 85.1 ms: 1.09x faster                                  |
| spectral_norm           | 100 ms                                                 | 91.5 ms: 1.09x faster                                  |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.09x faster                                  |
| scimark_sor             | 118 ms                                                 | 109 ms: 1.08x faster                                   |
| deepcopy_memo           | 37.0 us                                                | 34.3 us: 1.08x faster                                  |
| logging_format          | 6.68 us                                                | 6.22 us: 1.07x faster                                  |
| pickle_pure_python      | 306 us                                                 | 285 us: 1.07x faster                                   |
| pycparser               | 1.18 sec                                               | 1.10 sec: 1.07x faster                                 |
| hexiom                  | 6.37 ms                                                | 5.94 ms: 1.07x faster                                  |
| pathlib                 | 18.2 ms                                                | 17.0 ms: 1.07x faster                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.20 ms: 1.07x faster                                  |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                   |
| pylint                  | 465 ms                                                 | 435 ms: 1.07x faster                                   |
| raytrace                | 297 ms                                                 | 279 ms: 1.07x faster                                   |
| html5lib                | 64.5 ms                                                | 60.7 ms: 1.06x faster                                  |
| json                    | 4.94 ms                                                | 4.65 ms: 1.06x faster                                  |
| scimark_fft             | 328 ms                                                 | 309 ms: 1.06x faster                                   |
| logging_simple          | 6.03 us                                                | 5.72 us: 1.05x faster                                  |
| chaos                   | 69.2 ms                                                | 65.7 ms: 1.05x faster                                  |
| nqueens                 | 83.4 ms                                                | 79.1 ms: 1.05x faster                                  |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                   |
| go                      | 140 ms                                                 | 133 ms: 1.05x faster                                   |
| float                   | 77.2 ms                                                | 73.5 ms: 1.05x faster                                  |
| mdp                     | 2.62 sec                                               | 2.49 sec: 1.05x faster                                 |
| docutils                | 2.63 sec                                               | 2.51 sec: 1.05x faster                                 |
| bench_thread_pool       | 819 us                                                 | 781 us: 1.05x faster                                   |
| xml_etree_iterparse     | 104 ms                                                 | 99.3 ms: 1.05x faster                                  |
| regex_compile           | 138 ms                                                 | 132 ms: 1.05x faster                                   |
| sympy_expand            | 475 ms                                                 | 454 ms: 1.05x faster                                   |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                 |
| comprehensions          | 22.4 us                                                | 21.5 us: 1.04x faster                                  |
| coverage                | 100 ms                                                 | 96.0 ms: 1.04x faster                                  |
| logging_silent          | 101 ns                                                 | 97.0 ns: 1.04x faster                                  |
| tornado_http            | 96.3 ms                                                | 92.4 ms: 1.04x faster                                  |
| sympy_str               | 290 ms                                                 | 279 ms: 1.04x faster                                   |
| deepcopy                | 342 us                                                 | 328 us: 1.04x faster                                   |
| 2to3                    | 259 ms                                                 | 249 ms: 1.04x faster                                   |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.04x faster                                   |
| pprint_safe_repr        | 701 ms                                                 | 675 ms: 1.04x faster                                   |
| regex_v8                | 22.0 ms                                                | 21.3 ms: 1.03x faster                                  |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                   |
| sqlglot_optimize        | 53.1 ms                                                | 51.4 ms: 1.03x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                  |
| async_tree_cpu_io_mixed | 739 ms                                                 | 716 ms: 1.03x faster                                   |
| dulwich_log             | 63.7 ms                                                | 61.8 ms: 1.03x faster                                  |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.03x faster                                   |
| sqlalchemy_imperative   | 17.9 ms                                                | 17.4 ms: 1.03x faster                                  |
| fannkuch                | 388 ms                                                 | 378 ms: 1.03x faster                                   |
| genshi_text             | 21.6 ms                                                | 21.0 ms: 1.03x faster                                  |
| async_tree_memoization  | 627 ms                                                 | 612 ms: 1.02x faster                                   |
| sqlalchemy_declarative  | 138 ms                                                 | 135 ms: 1.02x faster                                   |
| mako                    | 10.1 ms                                                | 9.86 ms: 1.02x faster                                  |
| chameleon               | 6.47 ms                                                | 6.33 ms: 1.02x faster                                  |
| sympy_sum               | 167 ms                                                 | 163 ms: 1.02x faster                                   |
| async_tree_none         | 526 ms                                                 | 518 ms: 1.02x faster                                   |
| unpack_sequence         | 43.1 ns                                                | 42.5 ns: 1.01x faster                                  |
| async_tree_io           | 1.30 sec                                               | 1.28 sec: 1.01x faster                                 |
| pyflate                 | 418 ms                                                 | 414 ms: 1.01x faster                                   |
| gc_traversal            | 4.02 ms                                                | 3.98 ms: 1.01x faster                                  |
| regex_dna               | 204 ms                                                 | 202 ms: 1.01x faster                                   |
| scimark_monte_carlo     | 68.1 ms                                                | 67.6 ms: 1.01x faster                                  |
| telco                   | 6.58 ms                                                | 6.54 ms: 1.01x faster                                  |
| unpickle_list           | 4.91 us                                                | 4.88 us: 1.01x faster                                  |
| django_template         | 32.6 ms                                                | 32.4 ms: 1.01x faster                                  |
| deepcopy_reduce         | 2.94 us                                                | 2.97 us: 1.01x slower                                  |
| create_gc_cycles        | 1.49 ms                                                | 1.50 ms: 1.01x slower                                  |
| xml_etree_process       | 53.9 ms                                                | 55.0 ms: 1.02x slower                                  |
| thrift                  | 756 us                                                 | 780 us: 1.03x slower                                   |
| sqlite_synth            | 2.52 us                                                | 2.62 us: 1.04x slower                                  |
| python_startup          | 8.52 ms                                                | 8.91 ms: 1.05x slower                                  |
| xml_etree_generate      | 76.2 ms                                                | 79.9 ms: 1.05x slower                                  |
| pickle_list             | 4.11 us                                                | 4.31 us: 1.05x slower                                  |
| pickle_dict             | 31.1 us                                                | 32.9 us: 1.06x slower                                  |
| unpickle                | 13.7 us                                                | 14.6 us: 1.07x slower                                  |
| pickle                  | 10.1 us                                                | 10.9 us: 1.08x slower                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.60 ms: 1.10x slower                                  |
| async_generators        | 368 ms                                                 | 430 ms: 1.17x slower                                   |
| dask                    | 360 ms                                                 | 492 ms: 1.37x slower                                   |
| Geometric mean          | (ref)                                                  | 1.06x faster                                           |

Benchmark hidden because not significant (3): djangocms, crypto_pyaes, bench_mp_pool
Ignored benchmarks (5) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x
