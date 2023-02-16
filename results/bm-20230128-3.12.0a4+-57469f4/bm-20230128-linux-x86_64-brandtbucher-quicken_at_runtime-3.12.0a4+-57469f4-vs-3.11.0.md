
# Results vs. 3.11.0

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: 57469f4
- commit date: 2023-01-28
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 254 ms: 1.02x faster                                                       |
| docutils       | 2.60 sec                                               | 2.51 sec: 1.04x faster                                                     |
| html5lib       | 64.8 ms                                                | 61.4 ms: 1.06x faster                                                      |
| tornado_http   | 96.5 ms                                                | 94.3 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 197 ms                                                 | 192 ms: 1.02x faster                                                       |
| float          | 76.8 ms                                                | 75.1 ms: 1.02x faster                                                      |
| nbody          | 90.0 ms                                                | 92.3 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 131 ms: 1.04x faster                                                       |
| regex_v8       | 22.2 ms                                                | 22.7 ms: 1.02x slower                                                      |
| regex_effbot   | 3.46 ms                                                | 3.60 ms: 1.04x slower                                                      |
| regex_dna      | 203 ms                                                 | 219 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                  | 1.02x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.40 ms: 1.31x faster                                                      |
| unpickle_pure_python | 227 us                                                 | 208 us: 1.09x faster                                                       |
| json_loads           | 26.1 us                                                | 23.9 us: 1.09x faster                                                      |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                       |
| pickle_pure_python   | 308 us                                                 | 292 us: 1.05x faster                                                       |
| pickle_list          | 4.14 us                                                | 4.06 us: 1.02x faster                                                      |
| pickle_dict          | 31.2 us                                                | 30.8 us: 1.01x faster                                                      |
| pickle               | 9.90 us                                                | 9.98 us: 1.01x slower                                                      |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                                       |
| unpickle_list        | 4.99 us                                                | 5.07 us: 1.02x slower                                                      |
| xml_etree_generate   | 75.9 ms                                                | 77.5 ms: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (2): unpickle, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.70 ms: 1.01x slower                                                      |
| python_startup_no_site | 6.04 ms                                                | 6.23 ms: 1.03x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml     | 51.4 ms                                                | 46.4 ms: 1.11x faster                                                      |
| genshi_text    | 21.5 ms                                                | 20.6 ms: 1.04x faster                                                      |
| mako           | 9.83 ms                                                | 9.44 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 496 ms: 1.78x faster                                                       |
| json_dumps              | 12.4 ms                                                | 9.40 ms: 1.31x faster                                                      |
| scimark_sparse_mat_mult | 4.59 ms                                                | 3.94 ms: 1.16x faster                                                      |
| genshi_xml              | 51.4 ms                                                | 46.4 ms: 1.11x faster                                                      |
| unpickle_pure_python    | 227 us                                                 | 208 us: 1.09x faster                                                       |
| deltablue               | 3.66 ms                                                | 3.35 ms: 1.09x faster                                                      |
| json_loads              | 26.1 us                                                | 23.9 us: 1.09x faster                                                      |
| logging_silent          | 98.0 ns                                                | 90.2 ns: 1.09x faster                                                      |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                                       |
| sympy_str               | 291 ms                                                 | 270 ms: 1.08x faster                                                       |
| scimark_fft             | 325 ms                                                 | 302 ms: 1.08x faster                                                       |
| richards                | 46.1 ms                                                | 42.9 ms: 1.08x faster                                                      |
| nqueens                 | 83.8 ms                                                | 78.0 ms: 1.07x faster                                                      |
| mdp                     | 2.63 sec                                               | 2.45 sec: 1.07x faster                                                     |
| unpack_sequence         | 44.5 ns                                                | 41.7 ns: 1.07x faster                                                      |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.06x faster                                                       |
| html5lib                | 64.8 ms                                                | 61.4 ms: 1.06x faster                                                      |
| json                    | 4.87 ms                                                | 4.61 ms: 1.05x faster                                                      |
| pickle_pure_python      | 308 us                                                 | 292 us: 1.05x faster                                                       |
| deepcopy                | 341 us                                                 | 324 us: 1.05x faster                                                       |
| deepcopy_memo           | 35.8 us                                                | 34.0 us: 1.05x faster                                                      |
| sympy_integrate         | 21.0 ms                                                | 20.0 ms: 1.05x faster                                                      |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.05x faster                                                      |
| sympy_expand            | 475 ms                                                 | 454 ms: 1.05x faster                                                       |
| logging_simple          | 6.02 us                                                | 5.75 us: 1.05x faster                                                      |
| genshi_text             | 21.5 ms                                                | 20.6 ms: 1.04x faster                                                      |
| create_gc_cycles        | 1.52 ms                                                | 1.45 ms: 1.04x faster                                                      |
| bench_thread_pool       | 817 us                                                 | 783 us: 1.04x faster                                                       |
| crypto_pyaes            | 75.7 ms                                                | 72.6 ms: 1.04x faster                                                      |
| regex_compile           | 136 ms                                                 | 131 ms: 1.04x faster                                                       |
| mako                    | 9.83 ms                                                | 9.44 ms: 1.04x faster                                                      |
| chaos                   | 68.7 ms                                                | 65.9 ms: 1.04x faster                                                      |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.04x faster                                                      |
| pprint_safe_repr        | 706 ms                                                 | 681 ms: 1.04x faster                                                       |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.04x faster                                                     |
| docutils                | 2.60 sec                                               | 2.51 sec: 1.04x faster                                                     |
| deepcopy_reduce         | 3.02 us                                                | 2.91 us: 1.04x faster                                                      |
| sqlglot_optimize        | 52.7 ms                                                | 51.0 ms: 1.03x faster                                                      |
| raytrace                | 291 ms                                                 | 282 ms: 1.03x faster                                                       |
| hexiom                  | 6.34 ms                                                | 6.16 ms: 1.03x faster                                                      |
| pathlib                 | 18.1 ms                                                | 17.6 ms: 1.03x faster                                                      |
| pycparser               | 1.19 sec                                               | 1.16 sec: 1.03x faster                                                     |
| scimark_lu              | 108 ms                                                 | 105 ms: 1.02x faster                                                       |
| pidigits                | 197 ms                                                 | 192 ms: 1.02x faster                                                       |
| tornado_http            | 96.5 ms                                                | 94.3 ms: 1.02x faster                                                      |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                                       |
| float                   | 76.8 ms                                                | 75.1 ms: 1.02x faster                                                      |
| thrift                  | 760 us                                                 | 744 us: 1.02x faster                                                       |
| 2to3                    | 259 ms                                                 | 254 ms: 1.02x faster                                                       |
| spectral_norm           | 98.1 ms                                                | 96.1 ms: 1.02x faster                                                      |
| pickle_list             | 4.14 us                                                | 4.06 us: 1.02x faster                                                      |
| logging_format          | 6.48 us                                                | 6.37 us: 1.02x faster                                                      |
| dulwich_log             | 64.0 ms                                                | 62.9 ms: 1.02x faster                                                      |
| gc_traversal            | 3.82 ms                                                | 3.76 ms: 1.02x faster                                                      |
| telco                   | 6.43 ms                                                | 6.34 ms: 1.01x faster                                                      |
| pickle_dict             | 31.2 us                                                | 30.8 us: 1.01x faster                                                      |
| scimark_monte_carlo     | 68.0 ms                                                | 67.3 ms: 1.01x faster                                                      |
| coroutines              | 26.2 ms                                                | 26.0 ms: 1.01x faster                                                      |
| async_generators        | 356 ms                                                 | 355 ms: 1.00x faster                                                       |
| pickle                  | 9.90 us                                                | 9.98 us: 1.01x slower                                                      |
| generators              | 73.5 ms                                                | 74.4 ms: 1.01x slower                                                      |
| python_startup          | 8.58 ms                                                | 8.70 ms: 1.01x slower                                                      |
| xml_etree_iterparse     | 104 ms                                                 | 106 ms: 1.02x slower                                                       |
| unpickle_list           | 4.99 us                                                | 5.07 us: 1.02x slower                                                      |
| regex_v8                | 22.2 ms                                                | 22.7 ms: 1.02x slower                                                      |
| xml_etree_generate      | 75.9 ms                                                | 77.5 ms: 1.02x slower                                                      |
| nbody                   | 90.0 ms                                                | 92.3 ms: 1.03x slower                                                      |
| coverage                | 99.3 ms                                                | 102 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed | 736 ms                                                 | 755 ms: 1.03x slower                                                       |
| scimark_sor             | 115 ms                                                 | 118 ms: 1.03x slower                                                       |
| python_startup_no_site  | 6.04 ms                                                | 6.23 ms: 1.03x slower                                                      |
| pyflate                 | 419 ms                                                 | 432 ms: 1.03x slower                                                       |
| regex_effbot            | 3.46 ms                                                | 3.60 ms: 1.04x slower                                                      |
| sqlglot_transpile       | 1.65 ms                                                | 1.72 ms: 1.04x slower                                                      |
| sqlite_synth            | 2.48 us                                                | 2.59 us: 1.04x slower                                                      |
| sqlglot_parse           | 1.36 ms                                                | 1.43 ms: 1.05x slower                                                      |
| async_tree_memoization  | 624 ms                                                 | 661 ms: 1.06x slower                                                       |
| regex_dna               | 203 ms                                                 | 219 ms: 1.08x slower                                                       |
| dask                    | 365 ms                                                 | 511 ms: 1.40x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (11): unpickle, async_tree_none, djangocms, xml_etree_process, go, bench_mp_pool, async_tree_io, fannkuch, meteor_contest, django_template, chameleon
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230128-3.12.0a4+-57469f4/bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4.json: mypy
