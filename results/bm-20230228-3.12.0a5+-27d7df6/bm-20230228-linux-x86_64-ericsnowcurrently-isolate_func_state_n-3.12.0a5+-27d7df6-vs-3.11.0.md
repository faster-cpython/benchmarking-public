
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: isolate_func_state_n
- machine: linux-x86_64
- commit hash: 27d7df6
- commit date: 2023-02-28
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_func_state_n-3.12.0a5+-27d7df6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                              |
| chameleon      | 6.38 ms                                                | 6.34 ms: 1.01x faster                                                             |
| docutils       | 2.60 sec                                               | 2.55 sec: 1.02x faster                                                            |
| html5lib       | 64.8 ms                                                | 62.4 ms: 1.04x faster                                                             |
| tornado_http   | 96.5 ms                                                | 95.2 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_func_state_n-3.12.0a5+-27d7df6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                                              |
| float          | 76.8 ms                                                | 74.1 ms: 1.04x faster                                                             |
| nbody          | 90.0 ms                                                | 94.1 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_func_state_n-3.12.0a5+-27d7df6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 203 ms                                                 | 199 ms: 1.02x faster                                                              |
| regex_v8       | 22.2 ms                                                | 21.8 ms: 1.02x faster                                                             |
| regex_effbot   | 3.46 ms                                                | 3.57 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                      |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_func_state_n-3.12.0a5+-27d7df6 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.58 ms: 1.29x faster                                                             |
| unpickle_pure_python | 227 us                                                 | 202 us: 1.12x faster                                                              |
| json_loads           | 26.1 us                                                | 24.0 us: 1.09x faster                                                             |
| xml_etree_parse      | 160 ms                                                 | 150 ms: 1.07x faster                                                              |
| pickle_pure_python   | 308 us                                                 | 293 us: 1.05x faster                                                              |
| pickle_dict          | 31.2 us                                                | 30.6 us: 1.02x faster                                                             |
| pickle_list          | 4.14 us                                                | 4.07 us: 1.02x faster                                                             |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                                             |
| unpickle             | 13.3 us                                                | 13.7 us: 1.03x slower                                                             |
| xml_etree_process    | 53.7 ms                                                | 56.4 ms: 1.05x slower                                                             |
| xml_etree_generate   | 75.9 ms                                                | 81.7 ms: 1.08x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                      |

Benchmark hidden because not significant (2): unpickle_list, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_func_state_n-3.12.0a5+-27d7df6 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 9.04 ms: 1.05x slower                                                             |
| python_startup_no_site | 6.04 ms                                                | 6.56 ms: 1.09x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_func_state_n-3.12.0a5+-27d7df6 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 49.0 ms: 1.05x faster                                                             |
| mako            | 9.83 ms                                                | 9.88 ms: 1.01x slower                                                             |
| genshi_text     | 21.5 ms                                                | 21.8 ms: 1.01x slower                                                             |
| django_template | 32.3 ms                                                | 33.6 ms: 1.04x slower                                                             |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_func_state_n-3.12.0a5+-27d7df6 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.8 ms: 2.39x faster                                                             |
| asyncio_tcp             | 883 ms                                                 | 500 ms: 1.77x faster                                                              |
| json_dumps              | 12.4 ms                                                | 9.58 ms: 1.29x faster                                                             |
| mypy2                   | 420 ms                                                 | 335 ms: 1.25x faster                                                              |
| deltablue               | 3.66 ms                                                | 3.23 ms: 1.13x faster                                                             |
| unpickle_pure_python    | 227 us                                                 | 202 us: 1.12x faster                                                              |
| coroutines              | 26.2 ms                                                | 23.3 ms: 1.12x faster                                                             |
| json_loads              | 26.1 us                                                | 24.0 us: 1.09x faster                                                             |
| unpack_sequence         | 44.5 ns                                                | 41.2 ns: 1.08x faster                                                             |
| pycparser               | 1.19 sec                                               | 1.10 sec: 1.08x faster                                                            |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.07x faster                                                              |
| mdp                     | 2.63 sec                                               | 2.46 sec: 1.07x faster                                                            |
| xml_etree_parse         | 160 ms                                                 | 150 ms: 1.07x faster                                                              |
| spectral_norm           | 98.1 ms                                                | 93.0 ms: 1.05x faster                                                             |
| richards                | 46.1 ms                                                | 43.9 ms: 1.05x faster                                                             |
| pickle_pure_python      | 308 us                                                 | 293 us: 1.05x faster                                                              |
| genshi_xml              | 51.4 ms                                                | 49.0 ms: 1.05x faster                                                             |
| fannkuch                | 384 ms                                                 | 367 ms: 1.05x faster                                                              |
| scimark_fft             | 325 ms                                                 | 311 ms: 1.05x faster                                                              |
| json                    | 4.87 ms                                                | 4.66 ms: 1.04x faster                                                             |
| logging_silent          | 98.0 ns                                                | 94.0 ns: 1.04x faster                                                             |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                                             |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                                              |
| html5lib                | 64.8 ms                                                | 62.4 ms: 1.04x faster                                                             |
| nqueens                 | 83.8 ms                                                | 80.8 ms: 1.04x faster                                                             |
| float                   | 76.8 ms                                                | 74.1 ms: 1.04x faster                                                             |
| pyflate                 | 419 ms                                                 | 405 ms: 1.03x faster                                                              |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.44 ms: 1.03x faster                                                             |
| hexiom                  | 6.34 ms                                                | 6.14 ms: 1.03x faster                                                             |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                              |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.03x faster                                                             |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                                              |
| sqlglot_optimize        | 52.7 ms                                                | 51.3 ms: 1.03x faster                                                             |
| bench_thread_pool       | 817 us                                                 | 797 us: 1.02x faster                                                              |
| regex_dna               | 203 ms                                                 | 199 ms: 1.02x faster                                                              |
| crypto_pyaes            | 75.7 ms                                                | 74.2 ms: 1.02x faster                                                             |
| scimark_monte_carlo     | 68.0 ms                                                | 66.6 ms: 1.02x faster                                                             |
| sympy_expand            | 475 ms                                                 | 466 ms: 1.02x faster                                                              |
| regex_v8                | 22.2 ms                                                | 21.8 ms: 1.02x faster                                                             |
| pathlib                 | 18.1 ms                                                | 17.7 ms: 1.02x faster                                                             |
| docutils                | 2.60 sec                                               | 2.55 sec: 1.02x faster                                                            |
| pickle_dict             | 31.2 us                                                | 30.6 us: 1.02x faster                                                             |
| pickle_list             | 4.14 us                                                | 4.07 us: 1.02x faster                                                             |
| go                      | 140 ms                                                 | 138 ms: 1.02x faster                                                              |
| pprint_safe_repr        | 706 ms                                                 | 694 ms: 1.02x faster                                                              |
| pprint_pformat          | 1.46 sec                                               | 1.43 sec: 1.02x faster                                                            |
| sympy_integrate         | 21.0 ms                                                | 20.6 ms: 1.02x faster                                                             |
| logging_simple          | 6.02 us                                                | 5.93 us: 1.02x faster                                                             |
| sympy_str               | 291 ms                                                 | 287 ms: 1.02x faster                                                              |
| chaos                   | 68.7 ms                                                | 67.7 ms: 1.01x faster                                                             |
| tornado_http            | 96.5 ms                                                | 95.2 ms: 1.01x faster                                                             |
| meteor_contest          | 104 ms                                                 | 103 ms: 1.01x faster                                                              |
| async_tree_io           | 1.30 sec                                               | 1.29 sec: 1.01x faster                                                            |
| deepcopy_memo           | 35.8 us                                                | 35.4 us: 1.01x faster                                                             |
| coverage                | 99.3 ms                                                | 98.3 ms: 1.01x faster                                                             |
| async_tree_none         | 526 ms                                                 | 521 ms: 1.01x faster                                                              |
| dulwich_log             | 64.0 ms                                                | 63.4 ms: 1.01x faster                                                             |
| chameleon               | 6.38 ms                                                | 6.34 ms: 1.01x faster                                                             |
| create_gc_cycles        | 1.52 ms                                                | 1.51 ms: 1.01x faster                                                             |
| deepcopy                | 341 us                                                 | 340 us: 1.00x faster                                                              |
| gc_traversal            | 3.82 ms                                                | 3.84 ms: 1.01x slower                                                             |
| mako                    | 9.83 ms                                                | 9.88 ms: 1.01x slower                                                             |
| genshi_text             | 21.5 ms                                                | 21.8 ms: 1.01x slower                                                             |
| sympy_sum               | 166 ms                                                 | 168 ms: 1.01x slower                                                              |
| sqlalchemy_declarative  | 138 ms                                                 | 141 ms: 1.02x slower                                                              |
| thrift                  | 760 us                                                 | 772 us: 1.02x slower                                                              |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                                             |
| unpickle                | 13.3 us                                                | 13.7 us: 1.03x slower                                                             |
| scimark_lu              | 108 ms                                                 | 111 ms: 1.03x slower                                                              |
| regex_effbot            | 3.46 ms                                                | 3.57 ms: 1.03x slower                                                             |
| django_template         | 32.3 ms                                                | 33.6 ms: 1.04x slower                                                             |
| async_tree_memoization  | 624 ms                                                 | 653 ms: 1.05x slower                                                              |
| nbody                   | 90.0 ms                                                | 94.1 ms: 1.05x slower                                                             |
| xml_etree_process       | 53.7 ms                                                | 56.4 ms: 1.05x slower                                                             |
| python_startup          | 8.58 ms                                                | 9.04 ms: 1.05x slower                                                             |
| sqlite_synth            | 2.48 us                                                | 2.62 us: 1.05x slower                                                             |
| sqlglot_transpile       | 1.65 ms                                                | 1.74 ms: 1.05x slower                                                             |
| sqlglot_parse           | 1.36 ms                                                | 1.44 ms: 1.06x slower                                                             |
| xml_etree_generate      | 75.9 ms                                                | 81.7 ms: 1.08x slower                                                             |
| python_startup_no_site  | 6.04 ms                                                | 6.56 ms: 1.09x slower                                                             |
| async_generators        | 356 ms                                                 | 421 ms: 1.18x slower                                                              |
| dask                    | 365 ms                                                 | 508 ms: 1.39x slower                                                              |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                      |

Benchmark hidden because not significant (11): djangocms, regex_compile, logging_format, raytrace, bench_mp_pool, unpickle_list, xml_etree_iterparse, deepcopy_reduce, telco, sqlalchemy_imperative, async_tree_cpu_io_mixed
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230228-3.12.0a5+-27d7df6/bm-20230228-linux-x86_64-ericsnowcurrently-isolate_func_state_n-3.12.0a5+-27d7df6.json: comprehensions
