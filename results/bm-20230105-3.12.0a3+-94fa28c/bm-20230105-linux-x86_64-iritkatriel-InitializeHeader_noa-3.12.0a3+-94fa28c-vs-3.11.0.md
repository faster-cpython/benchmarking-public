
# Results vs. 3.11.0

- fork: iritkatriel
- ref: InitializeHeader_noa
- machine: linux-x86_64
- commit hash: 94fa28c
- commit date: 2023-01-05
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 254 ms: 1.02x faster                                                        |
| chameleon      | 6.38 ms                                                | 6.15 ms: 1.04x faster                                                       |
| docutils       | 2.60 sec                                               | 2.51 sec: 1.04x faster                                                      |
| html5lib       | 64.8 ms                                                | 60.0 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 73.0 ms: 1.05x faster                                                       |
| pidigits       | 197 ms                                                 | 197 ms: 1.00x slower                                                        |
| nbody          | 90.0 ms                                                | 95.7 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 130 ms: 1.05x faster                                                        |
| regex_v8       | 22.2 ms                                                | 22.5 ms: 1.01x slower                                                       |
| regex_dna      | 203 ms                                                 | 207 ms: 1.02x slower                                                        |
| regex_effbot   | 3.46 ms                                                | 3.61 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.28 ms: 1.33x faster                                                       |
| unpickle_pure_python | 227 us                                                 | 197 us: 1.15x faster                                                        |
| json_loads           | 26.1 us                                                | 23.7 us: 1.10x faster                                                       |
| xml_etree_parse      | 160 ms                                                 | 149 ms: 1.08x faster                                                        |
| pickle_pure_python   | 308 us                                                 | 287 us: 1.07x faster                                                        |
| unpickle             | 13.3 us                                                | 12.9 us: 1.03x faster                                                       |
| pickle_list          | 4.14 us                                                | 4.04 us: 1.02x faster                                                       |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                        |
| pickle_dict          | 31.2 us                                                | 31.0 us: 1.00x faster                                                       |
| xml_etree_process    | 53.7 ms                                                | 53.4 ms: 1.00x faster                                                       |
| xml_etree_generate   | 75.9 ms                                                | 76.5 ms: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                                |

Benchmark hidden because not significant (2): unpickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.49 ms: 1.01x faster                                                       |
| python_startup_no_site | 6.04 ms                                                | 6.08 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.9 ms: 1.10x faster                                                       |
| genshi_text     | 21.5 ms                                                | 20.3 ms: 1.06x faster                                                       |
| mako            | 9.83 ms                                                | 9.38 ms: 1.05x faster                                                       |
| django_template | 32.3 ms                                                | 32.8 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps              | 12.4 ms                                                | 9.28 ms: 1.33x faster                                                       |
| unpickle_pure_python    | 227 us                                                 | 197 us: 1.15x faster                                                        |
| deltablue               | 3.66 ms                                                | 3.29 ms: 1.11x faster                                                       |
| json_loads              | 26.1 us                                                | 23.7 us: 1.10x faster                                                       |
| genshi_xml              | 51.4 ms                                                | 46.9 ms: 1.10x faster                                                       |
| richards                | 46.1 ms                                                | 42.3 ms: 1.09x faster                                                       |
| unpack_sequence         | 44.5 ns                                                | 41.2 ns: 1.08x faster                                                       |
| html5lib                | 64.8 ms                                                | 60.0 ms: 1.08x faster                                                       |
| xml_etree_parse         | 160 ms                                                 | 149 ms: 1.08x faster                                                        |
| nqueens                 | 83.8 ms                                                | 77.8 ms: 1.08x faster                                                       |
| pickle_pure_python      | 308 us                                                 | 287 us: 1.07x faster                                                        |
| pyflate                 | 419 ms                                                 | 392 ms: 1.07x faster                                                        |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.06x faster                                                      |
| scimark_sor             | 115 ms                                                 | 108 ms: 1.06x faster                                                        |
| scimark_monte_carlo     | 68.0 ms                                                | 64.1 ms: 1.06x faster                                                       |
| genshi_text             | 21.5 ms                                                | 20.3 ms: 1.06x faster                                                       |
| logging_silent          | 98.0 ns                                                | 92.5 ns: 1.06x faster                                                       |
| json                    | 4.87 ms                                                | 4.60 ms: 1.06x faster                                                       |
| deepcopy_memo           | 35.8 us                                                | 33.9 us: 1.06x faster                                                       |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.36 ms: 1.05x faster                                                       |
| float                   | 76.8 ms                                                | 73.0 ms: 1.05x faster                                                       |
| pprint_safe_repr        | 706 ms                                                 | 671 ms: 1.05x faster                                                        |
| mako                    | 9.83 ms                                                | 9.38 ms: 1.05x faster                                                       |
| bench_thread_pool       | 817 us                                                 | 779 us: 1.05x faster                                                        |
| regex_compile           | 136 ms                                                 | 130 ms: 1.05x faster                                                        |
| logging_simple          | 6.02 us                                                | 5.78 us: 1.04x faster                                                       |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                                        |
| hexiom                  | 6.34 ms                                                | 6.10 ms: 1.04x faster                                                       |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                                        |
| chameleon               | 6.38 ms                                                | 6.15 ms: 1.04x faster                                                       |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                        |
| docutils                | 2.60 sec                                               | 2.51 sec: 1.04x faster                                                      |
| sqlglot_optimize        | 52.7 ms                                                | 50.9 ms: 1.04x faster                                                       |
| deepcopy                | 341 us                                                 | 330 us: 1.03x faster                                                        |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                                       |
| coroutines              | 26.2 ms                                                | 25.4 ms: 1.03x faster                                                       |
| sympy_str               | 291 ms                                                 | 282 ms: 1.03x faster                                                        |
| deepcopy_reduce         | 3.02 us                                                | 2.93 us: 1.03x faster                                                       |
| unpickle                | 13.3 us                                                | 12.9 us: 1.03x faster                                                       |
| pycparser               | 1.19 sec                                               | 1.15 sec: 1.03x faster                                                      |
| pickle_list             | 4.14 us                                                | 4.04 us: 1.02x faster                                                       |
| scimark_fft             | 325 ms                                                 | 318 ms: 1.02x faster                                                        |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                        |
| fannkuch                | 384 ms                                                 | 377 ms: 1.02x faster                                                        |
| 2to3                    | 259 ms                                                 | 254 ms: 1.02x faster                                                        |
| telco                   | 6.43 ms                                                | 6.30 ms: 1.02x faster                                                       |
| chaos                   | 68.7 ms                                                | 67.4 ms: 1.02x faster                                                       |
| dulwich_log             | 64.0 ms                                                | 62.8 ms: 1.02x faster                                                       |
| crypto_pyaes            | 75.7 ms                                                | 74.4 ms: 1.02x faster                                                       |
| raytrace                | 291 ms                                                 | 287 ms: 1.02x faster                                                        |
| meteor_contest          | 104 ms                                                 | 103 ms: 1.01x faster                                                        |
| thrift                  | 760 us                                                 | 750 us: 1.01x faster                                                        |
| spectral_norm           | 98.1 ms                                                | 97.1 ms: 1.01x faster                                                       |
| python_startup          | 8.58 ms                                                | 8.49 ms: 1.01x faster                                                       |
| sympy_sum               | 166 ms                                                 | 164 ms: 1.01x faster                                                        |
| async_generators        | 356 ms                                                 | 352 ms: 1.01x faster                                                        |
| logging_format          | 6.48 us                                                | 6.42 us: 1.01x faster                                                       |
| coverage                | 99.3 ms                                                | 98.8 ms: 1.00x faster                                                       |
| pickle_dict             | 31.2 us                                                | 31.0 us: 1.00x faster                                                       |
| xml_etree_process       | 53.7 ms                                                | 53.4 ms: 1.00x faster                                                       |
| pidigits                | 197 ms                                                 | 197 ms: 1.00x slower                                                        |
| python_startup_no_site  | 6.04 ms                                                | 6.08 ms: 1.01x slower                                                       |
| xml_etree_generate      | 75.9 ms                                                | 76.5 ms: 1.01x slower                                                       |
| regex_v8                | 22.2 ms                                                | 22.5 ms: 1.01x slower                                                       |
| django_template         | 32.3 ms                                                | 32.8 ms: 1.01x slower                                                       |
| scimark_lu              | 108 ms                                                 | 110 ms: 1.02x slower                                                        |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                      |
| regex_dna               | 203 ms                                                 | 207 ms: 1.02x slower                                                        |
| async_tree_cpu_io_mixed | 736 ms                                                 | 755 ms: 1.03x slower                                                        |
| sqlglot_transpile       | 1.65 ms                                                | 1.70 ms: 1.03x slower                                                       |
| mdp                     | 2.63 sec                                               | 2.72 sec: 1.04x slower                                                      |
| async_tree_memoization  | 624 ms                                                 | 647 ms: 1.04x slower                                                        |
| sqlglot_parse           | 1.36 ms                                                | 1.41 ms: 1.04x slower                                                       |
| regex_effbot            | 3.46 ms                                                | 3.61 ms: 1.04x slower                                                       |
| generators              | 73.5 ms                                                | 76.8 ms: 1.04x slower                                                       |
| sqlite_synth            | 2.48 us                                                | 2.60 us: 1.05x slower                                                       |
| nbody                   | 90.0 ms                                                | 95.7 ms: 1.06x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (6): djangocms, unpickle_list, bench_mp_pool, pathlib, async_tree_none, pickle
Ignored benchmarks (12) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230105-3.12.0a3+-94fa28c/bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c.json: mypy
