
# Results vs. 3.11.0

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: 34ba834
- commit date: 2023-01-18
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 256 ms: 1.01x faster                                                       |
| chameleon      | 6.38 ms                                                | 6.56 ms: 1.03x slower                                                      |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                     |
| html5lib       | 64.8 ms                                                | 61.4 ms: 1.06x faster                                                      |
| tornado_http   | 96.5 ms                                                | 94.7 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 74.3 ms: 1.03x faster                                                      |
| pidigits       | 197 ms                                                 | 198 ms: 1.00x slower                                                       |
| nbody          | 90.0 ms                                                | 92.5 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                  | 1.00x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 22.2 ms                                                | 21.1 ms: 1.05x faster                                                      |
| regex_compile  | 136 ms                                                 | 130 ms: 1.05x faster                                                       |
| regex_dna      | 203 ms                                                 | 201 ms: 1.01x faster                                                       |
| regex_effbot   | 3.46 ms                                                | 3.44 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.55 ms: 1.29x faster                                                      |
| unpickle_pure_python | 227 us                                                 | 209 us: 1.09x faster                                                       |
| xml_etree_parse      | 160 ms                                                 | 147 ms: 1.09x faster                                                       |
| json_loads           | 26.1 us                                                | 24.4 us: 1.07x faster                                                      |
| pickle_pure_python   | 308 us                                                 | 290 us: 1.06x faster                                                       |
| pickle_list          | 4.14 us                                                | 4.02 us: 1.03x faster                                                      |
| pickle_dict          | 31.2 us                                                | 30.6 us: 1.02x faster                                                      |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                       |
| xml_etree_process    | 53.7 ms                                                | 53.5 ms: 1.00x faster                                                      |
| pickle               | 9.90 us                                                | 10.0 us: 1.01x slower                                                      |
| xml_etree_generate   | 75.9 ms                                                | 77.2 ms: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                               |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.72 ms: 1.02x slower                                                      |
| python_startup_no_site | 6.04 ms                                                | 6.25 ms: 1.04x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 48.1 ms: 1.07x faster                                                      |
| genshi_text     | 21.5 ms                                                | 20.5 ms: 1.05x faster                                                      |
| mako            | 9.83 ms                                                | 9.57 ms: 1.03x faster                                                      |
| django_template | 32.3 ms                                                | 32.7 ms: 1.01x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 491 ms: 1.80x faster                                                       |
| json_dumps              | 12.4 ms                                                | 9.55 ms: 1.29x faster                                                      |
| deltablue               | 3.66 ms                                                | 3.32 ms: 1.10x faster                                                      |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.16 ms: 1.10x faster                                                      |
| unpickle_pure_python    | 227 us                                                 | 209 us: 1.09x faster                                                       |
| xml_etree_parse         | 160 ms                                                 | 147 ms: 1.09x faster                                                       |
| sympy_str               | 291 ms                                                 | 271 ms: 1.07x faster                                                       |
| json_loads              | 26.1 us                                                | 24.4 us: 1.07x faster                                                      |
| pycparser               | 1.19 sec                                               | 1.11 sec: 1.07x faster                                                     |
| genshi_xml              | 51.4 ms                                                | 48.1 ms: 1.07x faster                                                      |
| scimark_fft             | 325 ms                                                 | 305 ms: 1.07x faster                                                       |
| nqueens                 | 83.8 ms                                                | 78.7 ms: 1.06x faster                                                      |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.06x faster                                                       |
| logging_silent          | 98.0 ns                                                | 92.3 ns: 1.06x faster                                                      |
| pickle_pure_python      | 308 us                                                 | 290 us: 1.06x faster                                                       |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                                     |
| html5lib                | 64.8 ms                                                | 61.4 ms: 1.06x faster                                                      |
| richards                | 46.1 ms                                                | 43.8 ms: 1.05x faster                                                      |
| regex_v8                | 22.2 ms                                                | 21.1 ms: 1.05x faster                                                      |
| deepcopy_memo           | 35.8 us                                                | 34.0 us: 1.05x faster                                                      |
| chaos                   | 68.7 ms                                                | 65.3 ms: 1.05x faster                                                      |
| genshi_text             | 21.5 ms                                                | 20.5 ms: 1.05x faster                                                      |
| sympy_integrate         | 21.0 ms                                                | 20.0 ms: 1.05x faster                                                      |
| regex_compile           | 136 ms                                                 | 130 ms: 1.05x faster                                                       |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.05x faster                                                      |
| sympy_expand            | 475 ms                                                 | 455 ms: 1.05x faster                                                       |
| create_gc_cycles        | 1.52 ms                                                | 1.45 ms: 1.04x faster                                                      |
| pprint_safe_repr        | 706 ms                                                 | 677 ms: 1.04x faster                                                       |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.04x faster                                                      |
| json                    | 4.87 ms                                                | 4.67 ms: 1.04x faster                                                      |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                     |
| crypto_pyaes            | 75.7 ms                                                | 72.8 ms: 1.04x faster                                                      |
| deepcopy                | 341 us                                                 | 329 us: 1.04x faster                                                       |
| sqlglot_optimize        | 52.7 ms                                                | 50.8 ms: 1.04x faster                                                      |
| hexiom                  | 6.34 ms                                                | 6.12 ms: 1.04x faster                                                      |
| raytrace                | 291 ms                                                 | 282 ms: 1.03x faster                                                       |
| float                   | 76.8 ms                                                | 74.3 ms: 1.03x faster                                                      |
| bench_thread_pool       | 817 us                                                 | 791 us: 1.03x faster                                                       |
| pickle_list             | 4.14 us                                                | 4.02 us: 1.03x faster                                                      |
| logging_simple          | 6.02 us                                                | 5.85 us: 1.03x faster                                                      |
| spectral_norm           | 98.1 ms                                                | 95.4 ms: 1.03x faster                                                      |
| mako                    | 9.83 ms                                                | 9.57 ms: 1.03x faster                                                      |
| unpack_sequence         | 44.5 ns                                                | 43.3 ns: 1.03x faster                                                      |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                       |
| thrift                  | 760 us                                                 | 741 us: 1.02x faster                                                       |
| deepcopy_reduce         | 3.02 us                                                | 2.96 us: 1.02x faster                                                      |
| pickle_dict             | 31.2 us                                                | 30.6 us: 1.02x faster                                                      |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                       |
| tornado_http            | 96.5 ms                                                | 94.7 ms: 1.02x faster                                                      |
| fannkuch                | 384 ms                                                 | 378 ms: 1.02x faster                                                       |
| dulwich_log             | 64.0 ms                                                | 62.9 ms: 1.02x faster                                                      |
| pathlib                 | 18.1 ms                                                | 17.8 ms: 1.02x faster                                                      |
| coroutines              | 26.2 ms                                                | 25.8 ms: 1.02x faster                                                      |
| 2to3                    | 259 ms                                                 | 256 ms: 1.01x faster                                                       |
| regex_dna               | 203 ms                                                 | 201 ms: 1.01x faster                                                       |
| go                      | 140 ms                                                 | 139 ms: 1.01x faster                                                       |
| scimark_lu              | 108 ms                                                 | 107 ms: 1.01x faster                                                       |
| mdp                     | 2.63 sec                                               | 2.60 sec: 1.01x faster                                                     |
| logging_format          | 6.48 us                                                | 6.42 us: 1.01x faster                                                      |
| scimark_monte_carlo     | 68.0 ms                                                | 67.6 ms: 1.01x faster                                                      |
| regex_effbot            | 3.46 ms                                                | 3.44 ms: 1.00x faster                                                      |
| xml_etree_process       | 53.7 ms                                                | 53.5 ms: 1.00x faster                                                      |
| bench_mp_pool           | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                      |
| pidigits                | 197 ms                                                 | 198 ms: 1.00x slower                                                       |
| pyflate                 | 419 ms                                                 | 421 ms: 1.01x slower                                                       |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                                     |
| async_generators        | 356 ms                                                 | 359 ms: 1.01x slower                                                       |
| django_template         | 32.3 ms                                                | 32.7 ms: 1.01x slower                                                      |
| meteor_contest          | 104 ms                                                 | 106 ms: 1.01x slower                                                       |
| pickle                  | 9.90 us                                                | 10.0 us: 1.01x slower                                                      |
| python_startup          | 8.58 ms                                                | 8.72 ms: 1.02x slower                                                      |
| xml_etree_generate      | 75.9 ms                                                | 77.2 ms: 1.02x slower                                                      |
| coverage                | 99.3 ms                                                | 102 ms: 1.02x slower                                                       |
| nbody                   | 90.0 ms                                                | 92.5 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed | 736 ms                                                 | 756 ms: 1.03x slower                                                       |
| sqlglot_transpile       | 1.65 ms                                                | 1.70 ms: 1.03x slower                                                      |
| chameleon               | 6.38 ms                                                | 6.56 ms: 1.03x slower                                                      |
| sqlglot_parse           | 1.36 ms                                                | 1.41 ms: 1.03x slower                                                      |
| python_startup_no_site  | 6.04 ms                                                | 6.25 ms: 1.04x slower                                                      |
| generators              | 73.5 ms                                                | 76.3 ms: 1.04x slower                                                      |
| sqlite_synth            | 2.48 us                                                | 2.61 us: 1.05x slower                                                      |
| scimark_sor             | 115 ms                                                 | 121 ms: 1.05x slower                                                       |
| async_tree_memoization  | 624 ms                                                 | 659 ms: 1.06x slower                                                       |
| dask                    | 365 ms                                                 | 514 ms: 1.41x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (6): djangocms, gc_traversal, async_tree_none, unpickle_list, telco, unpickle
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230118-3.12.0a4+-34ba834/bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834.json: mypy
