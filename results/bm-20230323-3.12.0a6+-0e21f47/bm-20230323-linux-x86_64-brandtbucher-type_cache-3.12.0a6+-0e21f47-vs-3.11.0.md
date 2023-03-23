
# Results vs. 3.11.0

- fork: brandtbucher
- ref: type_cache
- machine: linux-x86_64
- commit hash: 0e21f47
- commit date: 2023-03-23
- overall geometric mean: 1.02x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.02x faster                                               |
| chameleon      | 6.38 ms                                                | 6.63 ms: 1.04x slower                                              |
| docutils       | 2.60 sec                                               | 2.57 sec: 1.01x faster                                             |
| html5lib       | 64.8 ms                                                | 62.4 ms: 1.04x faster                                              |
| tornado_http   | 96.5 ms                                                | 92.3 ms: 1.05x faster                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| pidigits       | 197 ms                                                 | 188 ms: 1.05x faster                                               |
| float          | 76.8 ms                                                | 73.7 ms: 1.04x faster                                              |
| nbody          | 90.0 ms                                                | 86.8 ms: 1.04x faster                                              |
| Geometric mean | (ref)                                                  | 1.04x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 134 ms: 1.02x faster                                               |
| regex_v8       | 22.2 ms                                                | 22.4 ms: 1.01x slower                                              |
| regex_dna      | 203 ms                                                 | 208 ms: 1.02x slower                                               |
| regex_effbot   | 3.46 ms                                                | 3.57 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                  | 1.01x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.71 ms: 1.27x faster                                              |
| unpickle_pure_python | 227 us                                                 | 200 us: 1.13x faster                                               |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                               |
| json_loads           | 26.1 us                                                | 24.2 us: 1.08x faster                                              |
| pickle_pure_python   | 308 us                                                 | 292 us: 1.06x faster                                               |
| xml_etree_iterparse  | 104 ms                                                 | 101 ms: 1.03x faster                                               |
| pickle_dict          | 31.2 us                                                | 30.7 us: 1.01x faster                                              |
| unpickle             | 13.3 us                                                | 13.8 us: 1.04x slower                                              |
| pickle_list          | 4.14 us                                                | 4.33 us: 1.05x slower                                              |
| pickle               | 9.90 us                                                | 10.4 us: 1.05x slower                                              |
| unpickle_list        | 4.99 us                                                | 5.28 us: 1.06x slower                                              |
| xml_etree_process    | 53.7 ms                                                | 58.0 ms: 1.08x slower                                              |
| xml_etree_generate   | 75.9 ms                                                | 82.1 ms: 1.08x slower                                              |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.87 ms: 1.03x slower                                              |
| python_startup_no_site | 6.04 ms                                                | 6.55 ms: 1.08x slower                                              |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 48.9 ms: 1.05x faster                                              |
| mako            | 9.83 ms                                                | 10.0 ms: 1.02x slower                                              |
| genshi_text     | 21.5 ms                                                | 22.0 ms: 1.02x slower                                              |
| django_template | 32.3 ms                                                | 34.0 ms: 1.05x slower                                              |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                       |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.3 ms: 2.51x faster                                              |
| asyncio_tcp             | 883 ms                                                 | 509 ms: 1.73x faster                                               |
| json_dumps              | 12.4 ms                                                | 9.71 ms: 1.27x faster                                              |
| mypy2                   | 420 ms                                                 | 337 ms: 1.24x faster                                               |
| coroutines              | 26.2 ms                                                | 22.7 ms: 1.15x faster                                              |
| unpickle_pure_python    | 227 us                                                 | 200 us: 1.13x faster                                               |
| deltablue               | 3.66 ms                                                | 3.32 ms: 1.10x faster                                              |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.21 ms: 1.09x faster                                              |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                               |
| json_loads              | 26.1 us                                                | 24.2 us: 1.08x faster                                              |
| scimark_sor             | 115 ms                                                 | 108 ms: 1.06x faster                                               |
| scimark_fft             | 325 ms                                                 | 306 ms: 1.06x faster                                               |
| pickle_pure_python      | 308 us                                                 | 292 us: 1.06x faster                                               |
| genshi_xml              | 51.4 ms                                                | 48.9 ms: 1.05x faster                                              |
| richards                | 46.1 ms                                                | 43.9 ms: 1.05x faster                                              |
| pidigits                | 197 ms                                                 | 188 ms: 1.05x faster                                               |
| spectral_norm           | 98.1 ms                                                | 93.6 ms: 1.05x faster                                              |
| tornado_http            | 96.5 ms                                                | 92.3 ms: 1.05x faster                                              |
| float                   | 76.8 ms                                                | 73.7 ms: 1.04x faster                                              |
| json                    | 4.87 ms                                                | 4.68 ms: 1.04x faster                                              |
| deepcopy_memo           | 35.8 us                                                | 34.4 us: 1.04x faster                                              |
| html5lib                | 64.8 ms                                                | 62.4 ms: 1.04x faster                                              |
| hexiom                  | 6.34 ms                                                | 6.11 ms: 1.04x faster                                              |
| nbody                   | 90.0 ms                                                | 86.8 ms: 1.04x faster                                              |
| xml_etree_iterparse     | 104 ms                                                 | 101 ms: 1.03x faster                                               |
| deepcopy                | 341 us                                                 | 331 us: 1.03x faster                                               |
| nqueens                 | 83.8 ms                                                | 81.2 ms: 1.03x faster                                              |
| crypto_pyaes            | 75.7 ms                                                | 73.7 ms: 1.03x faster                                              |
| 2to3                    | 259 ms                                                 | 253 ms: 1.02x faster                                               |
| create_gc_cycles        | 1.52 ms                                                | 1.48 ms: 1.02x faster                                              |
| go                      | 140 ms                                                 | 137 ms: 1.02x faster                                               |
| bench_thread_pool       | 817 us                                                 | 799 us: 1.02x faster                                               |
| chaos                   | 68.7 ms                                                | 67.3 ms: 1.02x faster                                              |
| logging_silent          | 98.0 ns                                                | 96.1 ns: 1.02x faster                                              |
| regex_compile           | 136 ms                                                 | 134 ms: 1.02x faster                                               |
| scimark_monte_carlo     | 68.0 ms                                                | 66.7 ms: 1.02x faster                                              |
| pprint_pformat          | 1.46 sec                                               | 1.43 sec: 1.02x faster                                             |
| sympy_integrate         | 21.0 ms                                                | 20.6 ms: 1.02x faster                                              |
| sympy_expand            | 475 ms                                                 | 468 ms: 1.02x faster                                               |
| sympy_str               | 291 ms                                                 | 287 ms: 1.01x faster                                               |
| pickle_dict             | 31.2 us                                                | 30.7 us: 1.01x faster                                              |
| logging_simple          | 6.02 us                                                | 5.95 us: 1.01x faster                                              |
| docutils                | 2.60 sec                                               | 2.57 sec: 1.01x faster                                             |
| pprint_safe_repr        | 706 ms                                                 | 698 ms: 1.01x faster                                               |
| sqlglot_optimize        | 52.7 ms                                                | 52.2 ms: 1.01x faster                                              |
| unpack_sequence         | 44.5 ns                                                | 44.7 ns: 1.00x slower                                              |
| mdp                     | 2.63 sec                                               | 2.64 sec: 1.00x slower                                             |
| pathlib                 | 18.1 ms                                                | 18.2 ms: 1.01x slower                                              |
| raytrace                | 291 ms                                                 | 293 ms: 1.01x slower                                               |
| regex_v8                | 22.2 ms                                                | 22.4 ms: 1.01x slower                                              |
| sqlglot_normalize       | 108 ms                                                 | 108 ms: 1.01x slower                                               |
| sympy_sum               | 166 ms                                                 | 167 ms: 1.01x slower                                               |
| dulwich_log             | 64.0 ms                                                | 64.6 ms: 1.01x slower                                              |
| deepcopy_reduce         | 3.02 us                                                | 3.05 us: 1.01x slower                                              |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.01x slower                                             |
| async_tree_none         | 526 ms                                                 | 535 ms: 1.02x slower                                               |
| async_tree_cpu_io_mixed | 736 ms                                                 | 750 ms: 1.02x slower                                               |
| mako                    | 9.83 ms                                                | 10.0 ms: 1.02x slower                                              |
| genshi_text             | 21.5 ms                                                | 22.0 ms: 1.02x slower                                              |
| regex_dna               | 203 ms                                                 | 208 ms: 1.02x slower                                               |
| regex_effbot            | 3.46 ms                                                | 3.57 ms: 1.03x slower                                              |
| python_startup          | 8.58 ms                                                | 8.87 ms: 1.03x slower                                              |
| pyflate                 | 419 ms                                                 | 434 ms: 1.04x slower                                               |
| unpickle                | 13.3 us                                                | 13.8 us: 1.04x slower                                              |
| chameleon               | 6.38 ms                                                | 6.63 ms: 1.04x slower                                              |
| pickle_list             | 4.14 us                                                | 4.33 us: 1.05x slower                                              |
| django_template         | 32.3 ms                                                | 34.0 ms: 1.05x slower                                              |
| pickle                  | 9.90 us                                                | 10.4 us: 1.05x slower                                              |
| sqlite_synth            | 2.48 us                                                | 2.62 us: 1.06x slower                                              |
| unpickle_list           | 4.99 us                                                | 5.28 us: 1.06x slower                                              |
| thrift                  | 760 us                                                 | 804 us: 1.06x slower                                               |
| sqlglot_transpile       | 1.65 ms                                                | 1.75 ms: 1.06x slower                                              |
| gc_traversal            | 3.82 ms                                                | 4.06 ms: 1.06x slower                                              |
| sqlglot_parse           | 1.36 ms                                                | 1.46 ms: 1.07x slower                                              |
| xml_etree_process       | 53.7 ms                                                | 58.0 ms: 1.08x slower                                              |
| xml_etree_generate      | 75.9 ms                                                | 82.1 ms: 1.08x slower                                              |
| async_tree_memoization  | 624 ms                                                 | 676 ms: 1.08x slower                                               |
| python_startup_no_site  | 6.04 ms                                                | 6.55 ms: 1.08x slower                                              |
| async_generators        | 356 ms                                                 | 416 ms: 1.17x slower                                               |
| dask                    | 365 ms                                                 | 515 ms: 1.41x slower                                               |
| Geometric mean          | (ref)                                                  | 1.02x faster                                                       |

Benchmark hidden because not significant (7): pycparser, telco, scimark_lu, logging_format, meteor_contest, bench_mp_pool, fannkuch
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, coverage, djangocms, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230323-3.12.0a6+-0e21f47/bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47.json: comprehensions
