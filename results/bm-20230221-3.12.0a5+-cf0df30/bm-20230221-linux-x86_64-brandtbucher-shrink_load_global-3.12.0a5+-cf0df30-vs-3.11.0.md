
# Results vs. 3.11.0

- fork: brandtbucher
- ref: shrink_load_global
- machine: linux-x86_64
- commit hash: cf0df30
- commit date: 2023-02-21
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 248 ms: 1.04x faster                                                       |
| html5lib       | 64.8 ms                                                | 61.0 ms: 1.06x faster                                                      |
| tornado_http   | 96.5 ms                                                | 94.5 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (2): chameleon, docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.3 ms: 1.06x faster                                                      |
| pidigits       | 197 ms                                                 | 192 ms: 1.02x faster                                                       |
| nbody          | 90.0 ms                                                | 94.2 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.07x faster                                                       |
| regex_v8       | 22.2 ms                                                | 22.5 ms: 1.01x slower                                                      |
| regex_dna      | 203 ms                                                 | 205 ms: 1.01x slower                                                       |
| regex_effbot   | 3.46 ms                                                | 3.63 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                  | 1.00x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.40 ms: 1.31x faster                                                      |
| unpickle_pure_python | 227 us                                                 | 198 us: 1.15x faster                                                       |
| pickle_pure_python   | 308 us                                                 | 282 us: 1.09x faster                                                       |
| json_loads           | 26.1 us                                                | 24.1 us: 1.08x faster                                                      |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                       |
| pickle_dict          | 31.2 us                                                | 30.4 us: 1.03x faster                                                      |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                       |
| unpickle_list        | 4.99 us                                                | 5.03 us: 1.01x slower                                                      |
| xml_etree_process    | 53.7 ms                                                | 54.5 ms: 1.02x slower                                                      |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                                      |
| xml_etree_generate   | 75.9 ms                                                | 80.0 ms: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                               |

Benchmark hidden because not significant (2): unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 9.01 ms: 1.05x slower                                                      |
| python_startup_no_site | 6.04 ms                                                | 6.54 ms: 1.08x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.5 ms: 1.11x faster                                                      |
| genshi_text     | 21.5 ms                                                | 20.6 ms: 1.05x faster                                                      |
| mako            | 9.83 ms                                                | 9.99 ms: 1.02x slower                                                      |
| django_template | 32.3 ms                                                | 33.3 ms: 1.03x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.9 ms: 2.46x faster                                                      |
| asyncio_tcp             | 883 ms                                                 | 502 ms: 1.76x faster                                                       |
| json_dumps              | 12.4 ms                                                | 9.40 ms: 1.31x faster                                                      |
| mypy2                   | 420 ms                                                 | 331 ms: 1.27x faster                                                       |
| coroutines              | 26.2 ms                                                | 21.9 ms: 1.19x faster                                                      |
| deltablue               | 3.66 ms                                                | 3.13 ms: 1.17x faster                                                      |
| unpickle_pure_python    | 227 us                                                 | 198 us: 1.15x faster                                                       |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.03 ms: 1.14x faster                                                      |
| genshi_xml              | 51.4 ms                                                | 46.5 ms: 1.11x faster                                                      |
| pickle_pure_python      | 308 us                                                 | 282 us: 1.09x faster                                                       |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.09x faster                                                       |
| richards                | 46.1 ms                                                | 42.6 ms: 1.08x faster                                                      |
| json_loads              | 26.1 us                                                | 24.1 us: 1.08x faster                                                      |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                                       |
| nqueens                 | 83.8 ms                                                | 77.5 ms: 1.08x faster                                                      |
| logging_silent          | 98.0 ns                                                | 91.0 ns: 1.08x faster                                                      |
| fannkuch                | 384 ms                                                 | 359 ms: 1.07x faster                                                       |
| mdp                     | 2.63 sec                                               | 2.45 sec: 1.07x faster                                                     |
| regex_compile           | 136 ms                                                 | 128 ms: 1.07x faster                                                       |
| html5lib                | 64.8 ms                                                | 61.0 ms: 1.06x faster                                                      |
| float                   | 76.8 ms                                                | 72.3 ms: 1.06x faster                                                      |
| json                    | 4.87 ms                                                | 4.58 ms: 1.06x faster                                                      |
| gc_traversal            | 3.82 ms                                                | 3.61 ms: 1.06x faster                                                      |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                                     |
| go                      | 140 ms                                                 | 133 ms: 1.06x faster                                                       |
| sympy_expand            | 475 ms                                                 | 452 ms: 1.05x faster                                                       |
| hexiom                  | 6.34 ms                                                | 6.03 ms: 1.05x faster                                                      |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.05x faster                                                      |
| genshi_text             | 21.5 ms                                                | 20.6 ms: 1.05x faster                                                      |
| logging_simple          | 6.02 us                                                | 5.75 us: 1.05x faster                                                      |
| crypto_pyaes            | 75.7 ms                                                | 72.3 ms: 1.05x faster                                                      |
| sqlglot_normalize       | 108 ms                                                 | 103 ms: 1.05x faster                                                       |
| pprint_safe_repr        | 706 ms                                                 | 675 ms: 1.05x faster                                                       |
| 2to3                    | 259 ms                                                 | 248 ms: 1.04x faster                                                       |
| scimark_fft             | 325 ms                                                 | 312 ms: 1.04x faster                                                       |
| pyflate                 | 419 ms                                                 | 401 ms: 1.04x faster                                                       |
| pycparser               | 1.19 sec                                               | 1.14 sec: 1.04x faster                                                     |
| sqlglot_optimize        | 52.7 ms                                                | 50.7 ms: 1.04x faster                                                      |
| spectral_norm           | 98.1 ms                                                | 94.5 ms: 1.04x faster                                                      |
| raytrace                | 291 ms                                                 | 281 ms: 1.04x faster                                                       |
| chaos                   | 68.7 ms                                                | 66.2 ms: 1.04x faster                                                      |
| bench_thread_pool       | 817 us                                                 | 788 us: 1.04x faster                                                       |
| sympy_str               | 291 ms                                                 | 281 ms: 1.03x faster                                                       |
| logging_format          | 6.48 us                                                | 6.26 us: 1.03x faster                                                      |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.03x faster                                                      |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                                      |
| pickle_dict             | 31.2 us                                                | 30.4 us: 1.03x faster                                                      |
| deepcopy                | 341 us                                                 | 333 us: 1.02x faster                                                       |
| pidigits                | 197 ms                                                 | 192 ms: 1.02x faster                                                       |
| async_tree_memoization  | 624 ms                                                 | 610 ms: 1.02x faster                                                       |
| coverage                | 99.3 ms                                                | 97.2 ms: 1.02x faster                                                      |
| tornado_http            | 96.5 ms                                                | 94.5 ms: 1.02x faster                                                      |
| meteor_contest          | 104 ms                                                 | 103 ms: 1.02x faster                                                       |
| deepcopy_memo           | 35.8 us                                                | 35.2 us: 1.02x faster                                                      |
| scimark_monte_carlo     | 68.0 ms                                                | 66.9 ms: 1.02x faster                                                      |
| dulwich_log             | 64.0 ms                                                | 63.0 ms: 1.01x faster                                                      |
| create_gc_cycles        | 1.52 ms                                                | 1.49 ms: 1.01x faster                                                      |
| deepcopy_reduce         | 3.02 us                                                | 2.98 us: 1.01x faster                                                      |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                                       |
| async_tree_none         | 526 ms                                                 | 521 ms: 1.01x faster                                                       |
| pathlib                 | 18.1 ms                                                | 18.0 ms: 1.01x faster                                                      |
| unpack_sequence         | 44.5 ns                                                | 44.7 ns: 1.01x slower                                                      |
| unpickle_list           | 4.99 us                                                | 5.03 us: 1.01x slower                                                      |
| regex_v8                | 22.2 ms                                                | 22.5 ms: 1.01x slower                                                      |
| regex_dna               | 203 ms                                                 | 205 ms: 1.01x slower                                                       |
| xml_etree_process       | 53.7 ms                                                | 54.5 ms: 1.02x slower                                                      |
| mako                    | 9.83 ms                                                | 9.99 ms: 1.02x slower                                                      |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                                      |
| django_template         | 32.3 ms                                                | 33.3 ms: 1.03x slower                                                      |
| sqlglot_transpile       | 1.65 ms                                                | 1.71 ms: 1.04x slower                                                      |
| sqlglot_parse           | 1.36 ms                                                | 1.42 ms: 1.04x slower                                                      |
| nbody                   | 90.0 ms                                                | 94.2 ms: 1.05x slower                                                      |
| regex_effbot            | 3.46 ms                                                | 3.63 ms: 1.05x slower                                                      |
| python_startup          | 8.58 ms                                                | 9.01 ms: 1.05x slower                                                      |
| xml_etree_generate      | 75.9 ms                                                | 80.0 ms: 1.05x slower                                                      |
| sqlite_synth            | 2.48 us                                                | 2.62 us: 1.06x slower                                                      |
| python_startup_no_site  | 6.04 ms                                                | 6.54 ms: 1.08x slower                                                      |
| async_generators        | 356 ms                                                 | 407 ms: 1.14x slower                                                       |
| dask                    | 365 ms                                                 | 497 ms: 1.36x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (14): unpickle, sqlalchemy_imperative, async_tree_io, pickle_list, docutils, telco, async_tree_cpu_io_mixed, sympy_sum, chameleon, bench_mp_pool, thrift, sqlalchemy_declarative, scimark_lu, djangocms
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
