
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 3adb23a
- commit date: 2023-03-18
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230318-linux-x86_64-python-main-3.12.0a6+-3adb23a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 249 ms: 1.04x faster                                   |
| docutils       | 2.60 sec                                               | 2.53 sec: 1.03x faster                                 |
| html5lib       | 64.8 ms                                                | 61.2 ms: 1.06x faster                                  |
| tornado_http   | 96.5 ms                                                | 91.2 ms: 1.06x faster                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230318-linux-x86_64-python-main-3.12.0a6+-3adb23a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 90.0 ms                                                | 86.0 ms: 1.05x faster                                  |
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                   |
| float          | 76.8 ms                                                | 73.9 ms: 1.04x faster                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230318-linux-x86_64-python-main-3.12.0a6+-3adb23a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_v8       | 22.2 ms                                                | 21.7 ms: 1.02x faster                                  |
| regex_compile  | 136 ms                                                 | 135 ms: 1.01x faster                                   |
| regex_dna      | 203 ms                                                 | 201 ms: 1.01x faster                                   |
| regex_effbot   | 3.46 ms                                                | 3.63 ms: 1.05x slower                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230318-linux-x86_64-python-main-3.12.0a6+-3adb23a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.57 ms: 1.29x faster                                  |
| unpickle_pure_python | 227 us                                                 | 198 us: 1.14x faster                                   |
| pickle_pure_python   | 308 us                                                 | 284 us: 1.09x faster                                   |
| json_loads           | 26.1 us                                                | 24.2 us: 1.08x faster                                  |
| xml_etree_parse      | 160 ms                                                 | 149 ms: 1.08x faster                                   |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| pickle_dict          | 31.2 us                                                | 31.3 us: 1.00x slower                                  |
| pickle_list          | 4.14 us                                                | 4.26 us: 1.03x slower                                  |
| xml_etree_process    | 53.7 ms                                                | 55.2 ms: 1.03x slower                                  |
| pickle               | 9.90 us                                                | 10.4 us: 1.05x slower                                  |
| xml_etree_generate   | 75.9 ms                                                | 80.4 ms: 1.06x slower                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230318-linux-x86_64-python-main-3.12.0a6+-3adb23a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.91 ms: 1.04x slower                                  |
| python_startup_no_site | 6.04 ms                                                | 6.52 ms: 1.08x slower                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230318-linux-x86_64-python-main-3.12.0a6+-3adb23a |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.1 ms: 1.09x faster                                  |
| genshi_text     | 21.5 ms                                                | 21.0 ms: 1.02x faster                                  |
| django_template | 32.3 ms                                                | 32.9 ms: 1.02x slower                                  |
| mako            | 9.83 ms                                                | 10.1 ms: 1.02x slower                                  |
| Geometric mean  | (ref)                                                  | 1.02x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230318-linux-x86_64-python-main-3.12.0a6+-3adb23a |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.3 ms: 2.50x faster                                  |
| asyncio_tcp             | 883 ms                                                 | 507 ms: 1.74x faster                                   |
| json_dumps              | 12.4 ms                                                | 9.57 ms: 1.29x faster                                  |
| mypy2                   | 420 ms                                                 | 332 ms: 1.27x faster                                   |
| deltablue               | 3.66 ms                                                | 3.17 ms: 1.15x faster                                  |
| coroutines              | 26.2 ms                                                | 22.8 ms: 1.15x faster                                  |
| unpickle_pure_python    | 227 us                                                 | 198 us: 1.14x faster                                   |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.15 ms: 1.10x faster                                  |
| richards                | 46.1 ms                                                | 41.9 ms: 1.10x faster                                  |
| genshi_xml              | 51.4 ms                                                | 47.1 ms: 1.09x faster                                  |
| pickle_pure_python      | 308 us                                                 | 284 us: 1.09x faster                                   |
| scimark_fft             | 325 ms                                                 | 300 ms: 1.08x faster                                   |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.08x faster                                   |
| json_loads              | 26.1 us                                                | 24.2 us: 1.08x faster                                  |
| xml_etree_parse         | 160 ms                                                 | 149 ms: 1.08x faster                                   |
| nqueens                 | 83.8 ms                                                | 77.9 ms: 1.08x faster                                  |
| pycparser               | 1.19 sec                                               | 1.11 sec: 1.07x faster                                 |
| spectral_norm           | 98.1 ms                                                | 92.7 ms: 1.06x faster                                  |
| html5lib                | 64.8 ms                                                | 61.2 ms: 1.06x faster                                  |
| tornado_http            | 96.5 ms                                                | 91.2 ms: 1.06x faster                                  |
| logging_simple          | 6.02 us                                                | 5.69 us: 1.06x faster                                  |
| deepcopy                | 341 us                                                 | 323 us: 1.06x faster                                   |
| json                    | 4.87 ms                                                | 4.62 ms: 1.05x faster                                  |
| deepcopy_memo           | 35.8 us                                                | 34.2 us: 1.05x faster                                  |
| nbody                   | 90.0 ms                                                | 86.0 ms: 1.05x faster                                  |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.04x faster                                  |
| 2to3                    | 259 ms                                                 | 249 ms: 1.04x faster                                   |
| sqlglot_normalize       | 108 ms                                                 | 103 ms: 1.04x faster                                   |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                   |
| chaos                   | 68.7 ms                                                | 66.0 ms: 1.04x faster                                  |
| deepcopy_reduce         | 3.02 us                                                | 2.90 us: 1.04x faster                                  |
| bench_thread_pool       | 817 us                                                 | 785 us: 1.04x faster                                   |
| raytrace                | 291 ms                                                 | 280 ms: 1.04x faster                                   |
| float                   | 76.8 ms                                                | 73.9 ms: 1.04x faster                                  |
| sympy_expand            | 475 ms                                                 | 458 ms: 1.04x faster                                   |
| hexiom                  | 6.34 ms                                                | 6.11 ms: 1.04x faster                                  |
| sqlglot_optimize        | 52.7 ms                                                | 50.9 ms: 1.04x faster                                  |
| scimark_monte_carlo     | 68.0 ms                                                | 65.7 ms: 1.03x faster                                  |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.03x faster                                 |
| logging_silent          | 98.0 ns                                                | 94.9 ns: 1.03x faster                                  |
| sympy_str               | 291 ms                                                 | 283 ms: 1.03x faster                                   |
| unpack_sequence         | 44.5 ns                                                | 43.2 ns: 1.03x faster                                  |
| pprint_safe_repr        | 706 ms                                                 | 686 ms: 1.03x faster                                   |
| gunicorn                | 1.12 ms                                                | 1.09 ms: 1.03x faster                                  |
| crypto_pyaes            | 75.7 ms                                                | 73.7 ms: 1.03x faster                                  |
| docutils                | 2.60 sec                                               | 2.53 sec: 1.03x faster                                 |
| go                      | 140 ms                                                 | 137 ms: 1.03x faster                                   |
| logging_format          | 6.48 us                                                | 6.31 us: 1.03x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                  |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| genshi_text             | 21.5 ms                                                | 21.0 ms: 1.02x faster                                  |
| pathlib                 | 18.1 ms                                                | 17.7 ms: 1.02x faster                                  |
| coverage                | 99.3 ms                                                | 97.0 ms: 1.02x faster                                  |
| regex_v8                | 22.2 ms                                                | 21.7 ms: 1.02x faster                                  |
| fannkuch                | 384 ms                                                 | 377 ms: 1.02x faster                                   |
| dulwich_log             | 64.0 ms                                                | 63.0 ms: 1.02x faster                                  |
| sqlalchemy_imperative   | 18.1 ms                                                | 17.8 ms: 1.01x faster                                  |
| regex_compile           | 136 ms                                                 | 135 ms: 1.01x faster                                   |
| create_gc_cycles        | 1.52 ms                                                | 1.50 ms: 1.01x faster                                  |
| sqlalchemy_declarative  | 138 ms                                                 | 137 ms: 1.01x faster                                   |
| meteor_contest          | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| regex_dna               | 203 ms                                                 | 201 ms: 1.01x faster                                   |
| pyflate                 | 419 ms                                                 | 414 ms: 1.01x faster                                   |
| mdp                     | 2.63 sec                                               | 2.61 sec: 1.01x faster                                 |
| pickle_dict             | 31.2 us                                                | 31.3 us: 1.00x slower                                  |
| scimark_lu              | 108 ms                                                 | 109 ms: 1.01x slower                                   |
| thrift                  | 760 us                                                 | 771 us: 1.01x slower                                   |
| async_tree_cpu_io_mixed | 736 ms                                                 | 747 ms: 1.02x slower                                   |
| django_template         | 32.3 ms                                                | 32.9 ms: 1.02x slower                                  |
| gc_traversal            | 3.82 ms                                                | 3.90 ms: 1.02x slower                                  |
| mako                    | 9.83 ms                                                | 10.1 ms: 1.02x slower                                  |
| pickle_list             | 4.14 us                                                | 4.26 us: 1.03x slower                                  |
| xml_etree_process       | 53.7 ms                                                | 55.2 ms: 1.03x slower                                  |
| async_tree_memoization  | 624 ms                                                 | 644 ms: 1.03x slower                                   |
| python_startup          | 8.58 ms                                                | 8.91 ms: 1.04x slower                                  |
| sqlglot_transpile       | 1.65 ms                                                | 1.71 ms: 1.04x slower                                  |
| sqlglot_parse           | 1.36 ms                                                | 1.43 ms: 1.05x slower                                  |
| regex_effbot            | 3.46 ms                                                | 3.63 ms: 1.05x slower                                  |
| pickle                  | 9.90 us                                                | 10.4 us: 1.05x slower                                  |
| sqlite_synth            | 2.48 us                                                | 2.62 us: 1.06x slower                                  |
| xml_etree_generate      | 75.9 ms                                                | 80.4 ms: 1.06x slower                                  |
| python_startup_no_site  | 6.04 ms                                                | 6.52 ms: 1.08x slower                                  |
| async_generators        | 356 ms                                                 | 413 ms: 1.16x slower                                   |
| dask                    | 365 ms                                                 | 501 ms: 1.37x slower                                   |
| Geometric mean          | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (9): async_tree_none, async_tree_io, chameleon, bench_mp_pool, telco, sympy_sum, unpickle_list, djangocms, unpickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230318-3.12.0a6+-3adb23a/bm-20230318-linux-x86_64-python-main-3.12.0a6+-3adb23a.json: comprehensions
