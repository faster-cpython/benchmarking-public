
# Results vs. 3.11.0

- fork: faster_cpython
- ref: nogil
- machine: linux-x86_64
- commit hash: 258cab1
- commit date: 2022-12-21
- overall geometric mean: 1.25x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 382 ms: 1.47x slower                                         |
| chameleon      | 6.38 ms                                                | 8.20 ms: 1.29x slower                                        |
| docutils       | 2.60 sec                                               | 5.20 sec: 2.00x slower                                       |
| html5lib       | 64.8 ms                                                | 81.7 ms: 1.26x slower                                        |
| tornado_http   | 96.5 ms                                                | 124 ms: 1.28x slower                                         |
| Geometric mean | (ref)                                                  | 1.44x slower                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 197 ms                                                 | 186 ms: 1.06x faster                                         |
| float          | 76.8 ms                                                | 104 ms: 1.36x slower                                         |
| nbody          | 90.0 ms                                                | 172 ms: 1.91x slower                                         |
| Geometric mean | (ref)                                                  | 1.35x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.46 ms                                                | 3.35 ms: 1.03x faster                                        |
| regex_dna      | 203 ms                                                 | 218 ms: 1.07x slower                                         |
| regex_v8       | 22.2 ms                                                | 24.1 ms: 1.08x slower                                        |
| regex_compile  | 136 ms                                                 | 186 ms: 1.37x slower                                         |
| Geometric mean | (ref)                                                  | 1.11x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_dict          | 31.2 us                                                | 25.3 us: 1.23x faster                                        |
| xml_etree_iterparse  | 104 ms                                                 | 95.5 ms: 1.09x faster                                        |
| xml_etree_parse      | 160 ms                                                 | 149 ms: 1.07x faster                                         |
| pickle_list          | 4.14 us                                                | 4.17 us: 1.01x slower                                        |
| pickle               | 9.90 us                                                | 10.0 us: 1.01x slower                                        |
| json_dumps           | 12.4 ms                                                | 13.4 ms: 1.09x slower                                        |
| pickle_pure_python   | 308 us                                                 | 346 us: 1.12x slower                                         |
| unpickle_pure_python | 227 us                                                 | 262 us: 1.16x slower                                         |
| xml_etree_generate   | 75.9 ms                                                | 87.8 ms: 1.16x slower                                        |
| unpickle_list        | 4.99 us                                                | 5.80 us: 1.16x slower                                        |
| json_loads           | 26.1 us                                                | 32.5 us: 1.25x slower                                        |
| xml_etree_process    | 53.7 ms                                                | 71.4 ms: 1.33x slower                                        |
| unpickle             | 13.3 us                                                | 18.6 us: 1.40x slower                                        |
| Geometric mean       | (ref)                                                  | 1.09x slower                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 6.04 ms                                                | 5.91 ms: 1.02x faster                                        |
| python_startup         | 8.58 ms                                                | 9.41 ms: 1.10x slower                                        |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 32.3 ms                                                | 42.6 ms: 1.32x slower                                        |
| genshi_xml      | 51.4 ms                                                | 73.6 ms: 1.43x slower                                        |
| mako            | 9.83 ms                                                | 16.4 ms: 1.67x slower                                        |
| genshi_text     | 21.5 ms                                                | 52.1 ms: 2.42x slower                                        |
| Geometric mean  | (ref)                                                  | 1.66x slower                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io           | 1.30 sec                                               | 829 ms: 1.57x faster                                         |
| async_tree_none         | 526 ms                                                 | 372 ms: 1.41x faster                                         |
| async_tree_memoization  | 624 ms                                                 | 460 ms: 1.36x faster                                         |
| pickle_dict             | 31.2 us                                                | 25.3 us: 1.23x faster                                        |
| async_tree_cpu_io_mixed | 736 ms                                                 | 614 ms: 1.20x faster                                         |
| richards                | 46.1 ms                                                | 39.3 ms: 1.17x faster                                        |
| xml_etree_iterparse     | 104 ms                                                 | 95.5 ms: 1.09x faster                                        |
| xml_etree_parse         | 160 ms                                                 | 149 ms: 1.07x faster                                         |
| pidigits                | 197 ms                                                 | 186 ms: 1.06x faster                                         |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                       |
| regex_effbot            | 3.46 ms                                                | 3.35 ms: 1.03x faster                                        |
| logging_silent          | 98.0 ns                                                | 96.0 ns: 1.02x faster                                        |
| python_startup_no_site  | 6.04 ms                                                | 5.91 ms: 1.02x faster                                        |
| bench_mp_pool           | 24.0 ms                                                | 23.8 ms: 1.01x faster                                        |
| pickle_list             | 4.14 us                                                | 4.17 us: 1.01x slower                                        |
| pickle                  | 9.90 us                                                | 10.0 us: 1.01x slower                                        |
| regex_dna               | 203 ms                                                 | 218 ms: 1.07x slower                                         |
| regex_v8                | 22.2 ms                                                | 24.1 ms: 1.08x slower                                        |
| json_dumps              | 12.4 ms                                                | 13.4 ms: 1.09x slower                                        |
| python_startup          | 8.58 ms                                                | 9.41 ms: 1.10x slower                                        |
| json                    | 4.87 ms                                                | 5.37 ms: 1.10x slower                                        |
| generators              | 73.5 ms                                                | 81.6 ms: 1.11x slower                                        |
| telco                   | 6.43 ms                                                | 7.15 ms: 1.11x slower                                        |
| sympy_expand            | 475 ms                                                 | 531 ms: 1.12x slower                                         |
| deepcopy_memo           | 35.8 us                                                | 40.1 us: 1.12x slower                                        |
| pickle_pure_python      | 308 us                                                 | 346 us: 1.12x slower                                         |
| go                      | 140 ms                                                 | 159 ms: 1.14x slower                                         |
| pycparser               | 1.19 sec                                               | 1.35 sec: 1.14x slower                                       |
| pathlib                 | 18.1 ms                                                | 20.6 ms: 1.14x slower                                        |
| deepcopy                | 341 us                                                 | 393 us: 1.15x slower                                         |
| sympy_str               | 291 ms                                                 | 335 ms: 1.15x slower                                         |
| logging_simple          | 6.02 us                                                | 6.95 us: 1.15x slower                                        |
| unpickle_pure_python    | 227 us                                                 | 262 us: 1.16x slower                                         |
| xml_etree_generate      | 75.9 ms                                                | 87.8 ms: 1.16x slower                                        |
| unpickle_list           | 4.99 us                                                | 5.80 us: 1.16x slower                                        |
| unpack_sequence         | 44.5 ns                                                | 52.4 ns: 1.18x slower                                        |
| mdp                     | 2.63 sec                                               | 3.10 sec: 1.18x slower                                       |
| logging_format          | 6.48 us                                                | 7.69 us: 1.19x slower                                        |
| deepcopy_reduce         | 3.02 us                                                | 3.63 us: 1.20x slower                                        |
| dulwich_log             | 64.0 ms                                                | 77.0 ms: 1.20x slower                                        |
| sympy_integrate         | 21.0 ms                                                | 25.4 ms: 1.21x slower                                        |
| meteor_contest          | 104 ms                                                 | 127 ms: 1.22x slower                                         |
| hexiom                  | 6.34 ms                                                | 7.74 ms: 1.22x slower                                        |
| djangocms               | 32.5 us                                                | 40.5 us: 1.24x slower                                        |
| json_loads              | 26.1 us                                                | 32.5 us: 1.25x slower                                        |
| scimark_sor             | 115 ms                                                 | 144 ms: 1.26x slower                                         |
| html5lib                | 64.8 ms                                                | 81.7 ms: 1.26x slower                                        |
| fannkuch                | 384 ms                                                 | 490 ms: 1.27x slower                                         |
| sympy_sum               | 166 ms                                                 | 212 ms: 1.28x slower                                         |
| tornado_http            | 96.5 ms                                                | 124 ms: 1.28x slower                                         |
| chameleon               | 6.38 ms                                                | 8.20 ms: 1.29x slower                                        |
| nqueens                 | 83.8 ms                                                | 109 ms: 1.30x slower                                         |
| thrift                  | 760 us                                                 | 992 us: 1.31x slower                                         |
| sqlite_synth            | 2.48 us                                                | 3.24 us: 1.31x slower                                        |
| sqlglot_optimize        | 52.7 ms                                                | 69.3 ms: 1.31x slower                                        |
| django_template         | 32.3 ms                                                | 42.6 ms: 1.32x slower                                        |
| scimark_fft             | 325 ms                                                 | 430 ms: 1.32x slower                                         |
| scimark_sparse_mat_mult | 4.59 ms                                                | 6.09 ms: 1.33x slower                                        |
| xml_etree_process       | 53.7 ms                                                | 71.4 ms: 1.33x slower                                        |
| sqlglot_normalize       | 108 ms                                                 | 144 ms: 1.34x slower                                         |
| pylint                  | 462 ms                                                 | 626 ms: 1.35x slower                                         |
| float                   | 76.8 ms                                                | 104 ms: 1.36x slower                                         |
| gunicorn                | 1.12 ms                                                | 1.52 ms: 1.36x slower                                        |
| regex_compile           | 136 ms                                                 | 186 ms: 1.37x slower                                         |
| aiohttp                 | 1.05 ms                                                | 1.44 ms: 1.37x slower                                        |
| scimark_lu              | 108 ms                                                 | 149 ms: 1.38x slower                                         |
| unpickle                | 13.3 us                                                | 18.6 us: 1.40x slower                                        |
| raytrace                | 291 ms                                                 | 416 ms: 1.43x slower                                         |
| genshi_xml              | 51.4 ms                                                | 73.6 ms: 1.43x slower                                        |
| bench_thread_pool       | 817 us                                                 | 1.19 ms: 1.45x slower                                        |
| spectral_norm           | 98.1 ms                                                | 143 ms: 1.45x slower                                         |
| 2to3                    | 259 ms                                                 | 382 ms: 1.47x slower                                         |
| deltablue               | 3.66 ms                                                | 5.41 ms: 1.48x slower                                        |
| scimark_monte_carlo     | 68.0 ms                                                | 101 ms: 1.48x slower                                         |
| chaos                   | 68.7 ms                                                | 102 ms: 1.48x slower                                         |
| pyflate                 | 419 ms                                                 | 636 ms: 1.52x slower                                         |
| sqlglot_transpile       | 1.65 ms                                                | 2.55 ms: 1.55x slower                                        |
| sqlglot_parse           | 1.36 ms                                                | 2.18 ms: 1.60x slower                                        |
| crypto_pyaes            | 75.7 ms                                                | 122 ms: 1.61x slower                                         |
| mako                    | 9.83 ms                                                | 16.4 ms: 1.67x slower                                        |
| flaskblogging           | 7.11 ms                                                | 12.1 ms: 1.71x slower                                        |
| async_generators        | 356 ms                                                 | 626 ms: 1.76x slower                                         |
| nbody                   | 90.0 ms                                                | 172 ms: 1.91x slower                                         |
| docutils                | 2.60 sec                                               | 5.20 sec: 2.00x slower                                       |
| genshi_text             | 21.5 ms                                                | 52.1 ms: 2.42x slower                                        |
| coroutines              | 26.2 ms                                                | 72.5 ms: 2.77x slower                                        |
| coverage                | 99.3 ms                                                | 553 ms: 5.57x slower                                         |
| Geometric mean          | (ref)                                                  | 1.25x slower                                                 |
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp, create_gc_cycles, dask, gc_traversal, mypy2, pprint_safe_repr, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221221-3.9.10-258cab1/bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1.json: mypy
