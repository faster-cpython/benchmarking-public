
# Results vs. base

- fork: faster-cpython
- ref: perf_perf
- machine: linux-x86_64
- commit hash: 2aab3df
- commit date: 2023-03-23
- overall geometric mean: 1.08x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230325-linux-x86_64-python-0708437ad043657f992c-3.12.0a6+-0708437 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                 | 271 ms: 1.07x slower                                                  |
| chameleon      | 6.47 ms                                                                | 7.07 ms: 1.09x slower                                                 |
| docutils       | 2.53 sec                                                               | 2.72 sec: 1.08x slower                                                |
| html5lib       | 62.2 ms                                                                | 68.3 ms: 1.10x slower                                                 |
| tornado_http   | 91.3 ms                                                                | 104 ms: 1.14x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.10x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230325-linux-x86_64-python-0708437ad043657f992c-3.12.0a6+-0708437 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 188 ms                                                                 | 189 ms: 1.00x slower                                                  |
| float          | 74.4 ms                                                                | 79.0 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230325-linux-x86_64-python-0708437ad043657f992c-3.12.0a6+-0708437 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.47 ms                                                                | 3.40 ms: 1.02x faster                                                 |
| regex_dna      | 204 ms                                                                 | 206 ms: 1.01x slower                                                  |
| regex_v8       | 22.1 ms                                                                | 22.7 ms: 1.03x slower                                                 |
| regex_compile  | 135 ms                                                                 | 145 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230325-linux-x86_64-python-0708437ad043657f992c-3.12.0a6+-0708437 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_list          | 4.43 us                                                                | 4.10 us: 1.08x faster                                                 |
| pickle_dict          | 32.4 us                                                                | 30.5 us: 1.06x faster                                                 |
| pickle               | 10.7 us                                                                | 10.3 us: 1.04x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                                 | 102 ms: 1.01x slower                                                  |
| xml_etree_parse      | 148 ms                                                                 | 150 ms: 1.01x slower                                                  |
| json_dumps           | 9.63 ms                                                                | 9.78 ms: 1.02x slower                                                 |
| json_loads           | 24.0 us                                                                | 24.4 us: 1.02x slower                                                 |
| unpickle_list        | 5.11 us                                                                | 5.20 us: 1.02x slower                                                 |
| unpickle             | 13.2 us                                                                | 13.6 us: 1.02x slower                                                 |
| xml_etree_generate   | 80.6 ms                                                                | 84.1 ms: 1.04x slower                                                 |
| xml_etree_process    | 56.0 ms                                                                | 60.6 ms: 1.08x slower                                                 |
| unpickle_pure_python | 203 us                                                                 | 238 us: 1.18x slower                                                  |
| pickle_pure_python   | 285 us                                                                 | 337 us: 1.18x slower                                                  |
| Geometric mean       | (ref)                                                                  | 1.03x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230325-linux-x86_64-python-0708437ad043657f992c-3.12.0a6+-0708437 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.50 ms                                                                | 6.88 ms: 1.06x slower                                                 |
| python_startup         | 8.79 ms                                                                | 9.52 ms: 1.08x slower                                                 |
| Geometric mean         | (ref)                                                                  | 1.07x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230325-linux-x86_64-python-0708437ad043657f992c-3.12.0a6+-0708437 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.93 ms                                                                | 10.6 ms: 1.07x slower                                                 |
| genshi_xml      | 47.6 ms                                                                | 52.2 ms: 1.10x slower                                                 |
| genshi_text     | 21.1 ms                                                                | 24.5 ms: 1.16x slower                                                 |
| django_template | 33.2 ms                                                                | 39.1 ms: 1.18x slower                                                 |
| Geometric mean  | (ref)                                                                  | 1.13x slower                                                          |

All benchmarks:
===============

| Benchmark               | bm-20230325-linux-x86_64-python-0708437ad043657f992c-3.12.0a6+-0708437 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_list             | 4.43 us                                                                | 4.10 us: 1.08x faster                                                 |
| pickle_dict             | 32.4 us                                                                | 30.5 us: 1.06x faster                                                 |
| scimark_sparse_mat_mult | 4.35 ms                                                                | 4.14 ms: 1.05x faster                                                 |
| scimark_fft             | 315 ms                                                                 | 302 ms: 1.05x faster                                                  |
| pickle                  | 10.7 us                                                                | 10.3 us: 1.04x faster                                                 |
| unpack_sequence         | 44.4 ns                                                                | 42.7 ns: 1.04x faster                                                 |
| scimark_lu              | 111 ms                                                                 | 108 ms: 1.03x faster                                                  |
| regex_effbot            | 3.47 ms                                                                | 3.40 ms: 1.02x faster                                                 |
| pidigits                | 188 ms                                                                 | 189 ms: 1.00x slower                                                  |
| xml_etree_iterparse     | 101 ms                                                                 | 102 ms: 1.01x slower                                                  |
| xml_etree_parse         | 148 ms                                                                 | 150 ms: 1.01x slower                                                  |
| fannkuch                | 382 ms                                                                 | 387 ms: 1.01x slower                                                  |
| regex_dna               | 204 ms                                                                 | 206 ms: 1.01x slower                                                  |
| pycparser               | 1.16 sec                                                               | 1.18 sec: 1.01x slower                                                |
| json_dumps              | 9.63 ms                                                                | 9.78 ms: 1.02x slower                                                 |
| generators              | 28.9 ms                                                                | 29.4 ms: 1.02x slower                                                 |
| json                    | 4.60 ms                                                                | 4.67 ms: 1.02x slower                                                 |
| create_gc_cycles        | 1.46 ms                                                                | 1.48 ms: 1.02x slower                                                 |
| json_loads              | 24.0 us                                                                | 24.4 us: 1.02x slower                                                 |
| unpickle_list           | 5.11 us                                                                | 5.20 us: 1.02x slower                                                 |
| crypto_pyaes            | 73.2 ms                                                                | 74.8 ms: 1.02x slower                                                 |
| unpickle                | 13.2 us                                                                | 13.6 us: 1.02x slower                                                 |
| regex_v8                | 22.1 ms                                                                | 22.7 ms: 1.03x slower                                                 |
| meteor_contest          | 102 ms                                                                 | 105 ms: 1.03x slower                                                  |
| asyncio_tcp             | 508 ms                                                                 | 522 ms: 1.03x slower                                                  |
| djangocms               | 32.3 us                                                                | 33.4 us: 1.03x slower                                                 |
| async_tree_memoization  | 657 ms                                                                 | 684 ms: 1.04x slower                                                  |
| xml_etree_generate      | 80.6 ms                                                                | 84.1 ms: 1.04x slower                                                 |
| chaos                   | 67.2 ms                                                                | 70.3 ms: 1.05x slower                                                 |
| thrift                  | 791 us                                                                 | 830 us: 1.05x slower                                                  |
| nqueens                 | 80.2 ms                                                                | 84.6 ms: 1.06x slower                                                 |
| bench_thread_pool       | 791 us                                                                 | 837 us: 1.06x slower                                                  |
| python_startup_no_site  | 6.50 ms                                                                | 6.88 ms: 1.06x slower                                                 |
| mdp                     | 2.50 sec                                                               | 2.65 sec: 1.06x slower                                                |
| coverage                | 97.1 ms                                                                | 103 ms: 1.06x slower                                                  |
| async_generators        | 411 ms                                                                 | 436 ms: 1.06x slower                                                  |
| float                   | 74.4 ms                                                                | 79.0 ms: 1.06x slower                                                 |
| gunicorn                | 1.09 ms                                                                | 1.16 ms: 1.06x slower                                                 |
| async_tree_io           | 1.30 sec                                                               | 1.39 sec: 1.06x slower                                                |
| pathlib                 | 17.8 ms                                                                | 19.0 ms: 1.07x slower                                                 |
| async_tree_cpu_io_mixed | 741 ms                                                                 | 793 ms: 1.07x slower                                                  |
| scimark_monte_carlo     | 67.2 ms                                                                | 71.9 ms: 1.07x slower                                                 |
| mako                    | 9.93 ms                                                                | 10.6 ms: 1.07x slower                                                 |
| 2to3                    | 252 ms                                                                 | 271 ms: 1.07x slower                                                  |
| sympy_sum               | 167 ms                                                                 | 179 ms: 1.07x slower                                                  |
| docutils                | 2.53 sec                                                               | 2.72 sec: 1.08x slower                                                |
| aiohttp                 | 1.01 ms                                                                | 1.09 ms: 1.08x slower                                                 |
| regex_compile           | 135 ms                                                                 | 145 ms: 1.08x slower                                                  |
| async_tree_none         | 525 ms                                                                 | 568 ms: 1.08x slower                                                  |
| xml_etree_process       | 56.0 ms                                                                | 60.6 ms: 1.08x slower                                                 |
| python_startup          | 8.79 ms                                                                | 9.52 ms: 1.08x slower                                                 |
| sympy_expand            | 462 ms                                                                 | 501 ms: 1.08x slower                                                  |
| sqlalchemy_declarative  | 137 ms                                                                 | 148 ms: 1.09x slower                                                  |
| sympy_str               | 286 ms                                                                 | 311 ms: 1.09x slower                                                  |
| sympy_integrate         | 20.5 ms                                                                | 22.4 ms: 1.09x slower                                                 |
| chameleon               | 6.47 ms                                                                | 7.07 ms: 1.09x slower                                                 |
| comprehensions          | 23.8 us                                                                | 26.0 us: 1.09x slower                                                 |
| sqlalchemy_imperative   | 17.8 ms                                                                | 19.5 ms: 1.09x slower                                                 |
| html5lib                | 62.2 ms                                                                | 68.3 ms: 1.10x slower                                                 |
| dask                    | 508 ms                                                                 | 557 ms: 1.10x slower                                                  |
| genshi_xml              | 47.6 ms                                                                | 52.2 ms: 1.10x slower                                                 |
| dulwich_log             | 63.3 ms                                                                | 69.9 ms: 1.10x slower                                                 |
| pprint_safe_repr        | 689 ms                                                                 | 770 ms: 1.12x slower                                                  |
| scimark_sor             | 113 ms                                                                 | 127 ms: 1.12x slower                                                  |
| pprint_pformat          | 1.41 sec                                                               | 1.59 sec: 1.12x slower                                                |
| deepcopy_reduce         | 2.98 us                                                                | 3.35 us: 1.13x slower                                                 |
| pyflate                 | 424 ms                                                                 | 478 ms: 1.13x slower                                                  |
| sqlglot_normalize       | 107 ms                                                                 | 121 ms: 1.13x slower                                                  |
| mypy2                   | 332 ms                                                                 | 378 ms: 1.14x slower                                                  |
| sqlglot_optimize        | 51.5 ms                                                                | 58.5 ms: 1.14x slower                                                 |
| tornado_http            | 91.3 ms                                                                | 104 ms: 1.14x slower                                                  |
| deepcopy                | 330 us                                                                 | 377 us: 1.14x slower                                                  |
| sqlglot_transpile       | 1.74 ms                                                                | 1.99 ms: 1.15x slower                                                 |
| sqlglot_parse           | 1.44 ms                                                                | 1.66 ms: 1.15x slower                                                 |
| genshi_text             | 21.1 ms                                                                | 24.5 ms: 1.16x slower                                                 |
| go                      | 139 ms                                                                 | 161 ms: 1.16x slower                                                  |
| spectral_norm           | 92.2 ms                                                                | 108 ms: 1.17x slower                                                  |
| unpickle_pure_python    | 203 us                                                                 | 238 us: 1.18x slower                                                  |
| django_template         | 33.2 ms                                                                | 39.1 ms: 1.18x slower                                                 |
| pickle_pure_python      | 285 us                                                                 | 337 us: 1.18x slower                                                  |
| gc_traversal            | 3.66 ms                                                                | 4.32 ms: 1.18x slower                                                 |
| raytrace                | 285 ms                                                                 | 337 ms: 1.18x slower                                                  |
| hexiom                  | 5.99 ms                                                                | 7.09 ms: 1.18x slower                                                 |
| deepcopy_memo           | 34.1 us                                                                | 41.2 us: 1.21x slower                                                 |
| coroutines              | 22.6 ms                                                                | 28.0 ms: 1.24x slower                                                 |
| richards                | 43.7 ms                                                                | 54.6 ms: 1.25x slower                                                 |
| logging_format          | 6.36 us                                                                | 8.20 us: 1.29x slower                                                 |
| logging_simple          | 5.79 us                                                                | 7.48 us: 1.29x slower                                                 |
| logging_silent          | 96.3 ns                                                                | 130 ns: 1.35x slower                                                  |
| deltablue               | 3.23 ms                                                                | 4.47 ms: 1.38x slower                                                 |
| Geometric mean          | (ref)                                                                  | 1.08x slower                                                          |

Benchmark hidden because not significant (4): sqlite_synth, bench_mp_pool, telco, nbody
