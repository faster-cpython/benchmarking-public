
# Results vs. 3.11.0

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 2e2a861
- commit date: 2023-02-06
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                |
| docutils       | 2.60 sec                                               | 2.49 sec: 1.04x faster                                              |
| html5lib       | 64.8 ms                                                | 60.3 ms: 1.07x faster                                               |
| tornado_http   | 96.5 ms                                                | 93.9 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 73.2 ms: 1.05x faster                                               |
| pidigits       | 197 ms                                                 | 203 ms: 1.03x slower                                                |
| nbody          | 90.0 ms                                                | 95.9 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                  | 1.02x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.07x faster                                                |
| regex_v8       | 22.2 ms                                                | 22.4 ms: 1.01x slower                                               |
| regex_effbot   | 3.46 ms                                                | 3.51 ms: 1.01x slower                                               |
| regex_dna      | 203 ms                                                 | 207 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.34 ms: 1.32x faster                                               |
| unpickle_pure_python | 227 us                                                 | 200 us: 1.13x faster                                                |
| json_loads           | 26.1 us                                                | 23.5 us: 1.11x faster                                               |
| xml_etree_parse      | 160 ms                                                 | 147 ms: 1.09x faster                                                |
| pickle_pure_python   | 308 us                                                 | 285 us: 1.08x faster                                                |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                |
| xml_etree_process    | 53.7 ms                                                | 53.4 ms: 1.00x faster                                               |
| pickle_dict          | 31.2 us                                                | 31.5 us: 1.01x slower                                               |
| pickle_list          | 4.14 us                                                | 4.22 us: 1.02x slower                                               |
| xml_etree_generate   | 75.9 ms                                                | 77.5 ms: 1.02x slower                                               |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                               |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                        |

Benchmark hidden because not significant (2): unpickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.96 ms: 1.04x slower                                               |
| python_startup_no_site | 6.04 ms                                                | 6.49 ms: 1.08x slower                                               |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.5 ms: 1.11x faster                                               |
| mako            | 9.83 ms                                                | 9.46 ms: 1.04x faster                                               |
| genshi_text     | 21.5 ms                                                | 20.7 ms: 1.04x faster                                               |
| django_template | 32.3 ms                                                | 32.5 ms: 1.00x slower                                               |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 494 ms: 1.79x faster                                                |
| json_dumps              | 12.4 ms                                                | 9.34 ms: 1.32x faster                                               |
| scimark_sparse_mat_mult | 4.59 ms                                                | 3.96 ms: 1.16x faster                                               |
| deltablue               | 3.66 ms                                                | 3.21 ms: 1.14x faster                                               |
| unpickle_pure_python    | 227 us                                                 | 200 us: 1.13x faster                                                |
| json_loads              | 26.1 us                                                | 23.5 us: 1.11x faster                                               |
| genshi_xml              | 51.4 ms                                                | 46.5 ms: 1.11x faster                                               |
| xml_etree_parse         | 160 ms                                                 | 147 ms: 1.09x faster                                                |
| richards                | 46.1 ms                                                | 42.6 ms: 1.08x faster                                               |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.08x faster                                                |
| json                    | 4.87 ms                                                | 4.50 ms: 1.08x faster                                               |
| pickle_pure_python      | 308 us                                                 | 285 us: 1.08x faster                                                |
| sympy_str               | 291 ms                                                 | 270 ms: 1.08x faster                                                |
| scimark_fft             | 325 ms                                                 | 302 ms: 1.08x faster                                                |
| html5lib                | 64.8 ms                                                | 60.3 ms: 1.07x faster                                               |
| nqueens                 | 83.8 ms                                                | 78.1 ms: 1.07x faster                                               |
| regex_compile           | 136 ms                                                 | 128 ms: 1.07x faster                                                |
| pprint_pformat          | 1.46 sec                                               | 1.36 sec: 1.07x faster                                              |
| coroutines              | 26.2 ms                                                | 24.5 ms: 1.07x faster                                               |
| sympy_integrate         | 21.0 ms                                                | 19.7 ms: 1.06x faster                                               |
| logging_silent          | 98.0 ns                                                | 92.2 ns: 1.06x faster                                               |
| pprint_safe_repr        | 706 ms                                                 | 666 ms: 1.06x faster                                                |
| pyflate                 | 419 ms                                                 | 395 ms: 1.06x faster                                                |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.06x faster                                                |
| fannkuch                | 384 ms                                                 | 363 ms: 1.06x faster                                                |
| logging_simple          | 6.02 us                                                | 5.69 us: 1.06x faster                                               |
| chaos                   | 68.7 ms                                                | 64.9 ms: 1.06x faster                                               |
| aiohttp                 | 1.05 ms                                                | 994 us: 1.06x faster                                                |
| hexiom                  | 6.34 ms                                                | 6.02 ms: 1.05x faster                                               |
| float                   | 76.8 ms                                                | 73.2 ms: 1.05x faster                                               |
| bench_thread_pool       | 817 us                                                 | 779 us: 1.05x faster                                                |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.04x faster                                               |
| sympy_expand            | 475 ms                                                 | 456 ms: 1.04x faster                                                |
| docutils                | 2.60 sec                                               | 2.49 sec: 1.04x faster                                              |
| telco                   | 6.43 ms                                                | 6.17 ms: 1.04x faster                                               |
| mako                    | 9.83 ms                                                | 9.46 ms: 1.04x faster                                               |
| genshi_text             | 21.5 ms                                                | 20.7 ms: 1.04x faster                                               |
| unpack_sequence         | 44.5 ns                                                | 42.8 ns: 1.04x faster                                               |
| pycparser               | 1.19 sec                                               | 1.14 sec: 1.04x faster                                              |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                                |
| sqlglot_optimize        | 52.7 ms                                                | 50.9 ms: 1.04x faster                                               |
| pathlib                 | 18.1 ms                                                | 17.5 ms: 1.03x faster                                               |
| create_gc_cycles        | 1.52 ms                                                | 1.47 ms: 1.03x faster                                               |
| deepcopy_memo           | 35.8 us                                                | 34.7 us: 1.03x faster                                               |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                |
| spectral_norm           | 98.1 ms                                                | 95.5 ms: 1.03x faster                                               |
| raytrace                | 291 ms                                                 | 284 ms: 1.03x faster                                                |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                |
| tornado_http            | 96.5 ms                                                | 93.9 ms: 1.03x faster                                               |
| thrift                  | 760 us                                                 | 740 us: 1.03x faster                                                |
| coverage                | 99.3 ms                                                | 96.8 ms: 1.03x faster                                               |
| logging_format          | 6.48 us                                                | 6.32 us: 1.03x faster                                               |
| dulwich_log             | 64.0 ms                                                | 62.4 ms: 1.02x faster                                               |
| deepcopy                | 341 us                                                 | 334 us: 1.02x faster                                                |
| scimark_monte_carlo     | 68.0 ms                                                | 66.6 ms: 1.02x faster                                               |
| scimark_lu              | 108 ms                                                 | 106 ms: 1.02x faster                                                |
| deepcopy_reduce         | 3.02 us                                                | 2.97 us: 1.02x faster                                               |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                                |
| async_generators        | 356 ms                                                 | 352 ms: 1.01x faster                                                |
| xml_etree_process       | 53.7 ms                                                | 53.4 ms: 1.00x faster                                               |
| django_template         | 32.3 ms                                                | 32.5 ms: 1.00x slower                                               |
| regex_v8                | 22.2 ms                                                | 22.4 ms: 1.01x slower                                               |
| mdp                     | 2.63 sec                                               | 2.65 sec: 1.01x slower                                              |
| pickle_dict             | 31.2 us                                                | 31.5 us: 1.01x slower                                               |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.01x slower                                              |
| gc_traversal            | 3.82 ms                                                | 3.87 ms: 1.01x slower                                               |
| regex_effbot            | 3.46 ms                                                | 3.51 ms: 1.01x slower                                               |
| pickle_list             | 4.14 us                                                | 4.22 us: 1.02x slower                                               |
| regex_dna               | 203 ms                                                 | 207 ms: 1.02x slower                                                |
| xml_etree_generate      | 75.9 ms                                                | 77.5 ms: 1.02x slower                                               |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                               |
| async_tree_cpu_io_mixed | 736 ms                                                 | 757 ms: 1.03x slower                                                |
| pidigits                | 197 ms                                                 | 203 ms: 1.03x slower                                                |
| sqlglot_parse           | 1.36 ms                                                | 1.40 ms: 1.03x slower                                               |
| sqlglot_transpile       | 1.65 ms                                                | 1.70 ms: 1.03x slower                                               |
| python_startup          | 8.58 ms                                                | 8.96 ms: 1.04x slower                                               |
| sqlite_synth            | 2.48 us                                                | 2.61 us: 1.05x slower                                               |
| nbody                   | 90.0 ms                                                | 95.9 ms: 1.07x slower                                               |
| generators              | 73.5 ms                                                | 78.7 ms: 1.07x slower                                               |
| python_startup_no_site  | 6.04 ms                                                | 6.49 ms: 1.08x slower                                               |
| dask                    | 365 ms                                                 | 493 ms: 1.35x slower                                                |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (9): djangocms, unpickle, chameleon, async_tree_none, async_tree_memoization, unpickle_list, crypto_pyaes, bench_mp_pool, meteor_contest
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230206-3.12.0a4+-2e2a861/bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861.json: mypy
