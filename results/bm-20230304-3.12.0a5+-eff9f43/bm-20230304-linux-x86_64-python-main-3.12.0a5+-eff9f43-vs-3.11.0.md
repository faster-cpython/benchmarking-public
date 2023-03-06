
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: eff9f43
- commit date: 2023-03-04
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230304-linux-x86_64-python-main-3.12.0a5+-eff9f43 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 250 ms: 1.04x faster                                   |
| chameleon      | 6.38 ms                                                | 6.42 ms: 1.01x slower                                  |
| docutils       | 2.60 sec                                               | 2.56 sec: 1.02x faster                                 |
| html5lib       | 64.8 ms                                                | 61.4 ms: 1.06x faster                                  |
| tornado_http   | 96.5 ms                                                | 94.9 ms: 1.02x faster                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230304-linux-x86_64-python-main-3.12.0a5+-eff9f43 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 197 ms                                                 | 190 ms: 1.04x faster                                   |
| float          | 76.8 ms                                                | 74.6 ms: 1.03x faster                                  |
| nbody          | 90.0 ms                                                | 94.0 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230304-linux-x86_64-python-main-3.12.0a5+-eff9f43 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 133 ms: 1.02x faster                                   |
| regex_v8       | 22.2 ms                                                | 21.8 ms: 1.02x faster                                  |
| regex_effbot   | 3.46 ms                                                | 3.40 ms: 1.02x faster                                  |
| regex_dna      | 203 ms                                                 | 209 ms: 1.03x slower                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230304-linux-x86_64-python-main-3.12.0a5+-eff9f43 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.56 ms: 1.29x faster                                  |
| unpickle_pure_python | 227 us                                                 | 199 us: 1.14x faster                                   |
| json_loads           | 26.1 us                                                | 23.9 us: 1.09x faster                                  |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                   |
| pickle_pure_python   | 308 us                                                 | 291 us: 1.06x faster                                   |
| pickle_list          | 4.14 us                                                | 4.05 us: 1.02x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| pickle_dict          | 31.2 us                                                | 31.5 us: 1.01x slower                                  |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                  |
| xml_etree_process    | 53.7 ms                                                | 55.4 ms: 1.03x slower                                  |
| unpickle             | 13.3 us                                                | 13.7 us: 1.03x slower                                  |
| unpickle_list        | 4.99 us                                                | 5.22 us: 1.05x slower                                  |
| xml_etree_generate   | 75.9 ms                                                | 81.3 ms: 1.07x slower                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230304-linux-x86_64-python-main-3.12.0a5+-eff9f43 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 9.03 ms: 1.05x slower                                  |
| python_startup_no_site | 6.04 ms                                                | 6.55 ms: 1.09x slower                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230304-linux-x86_64-python-main-3.12.0a5+-eff9f43 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 48.6 ms: 1.06x faster                                  |
| genshi_text     | 21.5 ms                                                | 21.2 ms: 1.02x faster                                  |
| mako            | 9.83 ms                                                | 10.1 ms: 1.02x slower                                  |
| django_template | 32.3 ms                                                | 33.2 ms: 1.03x slower                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230304-linux-x86_64-python-main-3.12.0a5+-eff9f43 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.6 ms: 2.40x faster                                  |
| asyncio_tcp             | 883 ms                                                 | 508 ms: 1.74x faster                                   |
| json_dumps              | 12.4 ms                                                | 9.56 ms: 1.29x faster                                  |
| mypy2                   | 420 ms                                                 | 334 ms: 1.26x faster                                   |
| unpickle_pure_python    | 227 us                                                 | 199 us: 1.14x faster                                   |
| deltablue               | 3.66 ms                                                | 3.20 ms: 1.14x faster                                  |
| coroutines              | 26.2 ms                                                | 23.5 ms: 1.11x faster                                  |
| json_loads              | 26.1 us                                                | 23.9 us: 1.09x faster                                  |
| richards                | 46.1 ms                                                | 42.6 ms: 1.08x faster                                  |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                   |
| pycparser               | 1.19 sec                                               | 1.10 sec: 1.07x faster                                 |
| json                    | 4.87 ms                                                | 4.59 ms: 1.06x faster                                  |
| pickle_pure_python      | 308 us                                                 | 291 us: 1.06x faster                                   |
| genshi_xml              | 51.4 ms                                                | 48.6 ms: 1.06x faster                                  |
| scimark_sor             | 115 ms                                                 | 109 ms: 1.06x faster                                   |
| mdp                     | 2.63 sec                                               | 2.49 sec: 1.06x faster                                 |
| html5lib                | 64.8 ms                                                | 61.4 ms: 1.06x faster                                  |
| go                      | 140 ms                                                 | 133 ms: 1.06x faster                                   |
| logging_silent          | 98.0 ns                                                | 93.2 ns: 1.05x faster                                  |
| deepcopy_memo           | 35.8 us                                                | 34.4 us: 1.04x faster                                  |
| pidigits                | 197 ms                                                 | 190 ms: 1.04x faster                                   |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                  |
| fannkuch                | 384 ms                                                 | 371 ms: 1.04x faster                                   |
| deepcopy                | 341 us                                                 | 329 us: 1.04x faster                                   |
| 2to3                    | 259 ms                                                 | 250 ms: 1.04x faster                                   |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.04x faster                                 |
| logging_simple          | 6.02 us                                                | 5.83 us: 1.03x faster                                  |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                   |
| unpack_sequence         | 44.5 ns                                                | 43.2 ns: 1.03x faster                                  |
| float                   | 76.8 ms                                                | 74.6 ms: 1.03x faster                                  |
| bench_thread_pool       | 817 us                                                 | 794 us: 1.03x faster                                   |
| gunicorn                | 1.12 ms                                                | 1.09 ms: 1.03x faster                                  |
| pprint_safe_repr        | 706 ms                                                 | 687 ms: 1.03x faster                                   |
| deepcopy_reduce         | 3.02 us                                                | 2.94 us: 1.03x faster                                  |
| sqlglot_optimize        | 52.7 ms                                                | 51.3 ms: 1.03x faster                                  |
| hexiom                  | 6.34 ms                                                | 6.18 ms: 1.02x faster                                  |
| pickle_list             | 4.14 us                                                | 4.05 us: 1.02x faster                                  |
| regex_compile           | 136 ms                                                 | 133 ms: 1.02x faster                                   |
| sympy_expand            | 475 ms                                                 | 466 ms: 1.02x faster                                   |
| regex_v8                | 22.2 ms                                                | 21.8 ms: 1.02x faster                                  |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| nqueens                 | 83.8 ms                                                | 82.2 ms: 1.02x faster                                  |
| tornado_http            | 96.5 ms                                                | 94.9 ms: 1.02x faster                                  |
| docutils                | 2.60 sec                                               | 2.56 sec: 1.02x faster                                 |
| regex_effbot            | 3.46 ms                                                | 3.40 ms: 1.02x faster                                  |
| genshi_text             | 21.5 ms                                                | 21.2 ms: 1.02x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 20.7 ms: 1.01x faster                                  |
| scimark_fft             | 325 ms                                                 | 322 ms: 1.01x faster                                   |
| dulwich_log             | 64.0 ms                                                | 63.2 ms: 1.01x faster                                  |
| sympy_str               | 291 ms                                                 | 288 ms: 1.01x faster                                   |
| coverage                | 99.3 ms                                                | 98.3 ms: 1.01x faster                                  |
| chaos                   | 68.7 ms                                                | 68.1 ms: 1.01x faster                                  |
| spectral_norm           | 98.1 ms                                                | 97.3 ms: 1.01x faster                                  |
| create_gc_cycles        | 1.52 ms                                                | 1.50 ms: 1.01x faster                                  |
| crypto_pyaes            | 75.7 ms                                                | 75.2 ms: 1.01x faster                                  |
| gc_traversal            | 3.82 ms                                                | 3.84 ms: 1.01x slower                                  |
| chameleon               | 6.38 ms                                                | 6.42 ms: 1.01x slower                                  |
| pickle_dict             | 31.2 us                                                | 31.5 us: 1.01x slower                                  |
| async_tree_cpu_io_mixed | 736 ms                                                 | 745 ms: 1.01x slower                                   |
| pyflate                 | 419 ms                                                 | 424 ms: 1.01x slower                                   |
| sympy_sum               | 166 ms                                                 | 168 ms: 1.01x slower                                   |
| raytrace                | 291 ms                                                 | 298 ms: 1.02x slower                                   |
| thrift                  | 760 us                                                 | 777 us: 1.02x slower                                   |
| mako                    | 9.83 ms                                                | 10.1 ms: 1.02x slower                                  |
| regex_dna               | 203 ms                                                 | 209 ms: 1.03x slower                                   |
| django_template         | 32.3 ms                                                | 33.2 ms: 1.03x slower                                  |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                  |
| telco                   | 6.43 ms                                                | 6.62 ms: 1.03x slower                                  |
| xml_etree_process       | 53.7 ms                                                | 55.4 ms: 1.03x slower                                  |
| unpickle                | 13.3 us                                                | 13.7 us: 1.03x slower                                  |
| scimark_lu              | 108 ms                                                 | 112 ms: 1.04x slower                                   |
| nbody                   | 90.0 ms                                                | 94.0 ms: 1.04x slower                                  |
| async_tree_memoization  | 624 ms                                                 | 653 ms: 1.05x slower                                   |
| unpickle_list           | 4.99 us                                                | 5.22 us: 1.05x slower                                  |
| sqlglot_transpile       | 1.65 ms                                                | 1.74 ms: 1.05x slower                                  |
| python_startup          | 8.58 ms                                                | 9.03 ms: 1.05x slower                                  |
| sqlite_synth            | 2.48 us                                                | 2.63 us: 1.06x slower                                  |
| sqlglot_parse           | 1.36 ms                                                | 1.45 ms: 1.06x slower                                  |
| xml_etree_generate      | 75.9 ms                                                | 81.3 ms: 1.07x slower                                  |
| python_startup_no_site  | 6.04 ms                                                | 6.55 ms: 1.09x slower                                  |
| async_generators        | 356 ms                                                 | 421 ms: 1.18x slower                                   |
| dask                    | 365 ms                                                 | 507 ms: 1.39x slower                                   |
| Geometric mean          | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (11): async_tree_none, async_tree_io, sqlalchemy_imperative, pathlib, djangocms, meteor_contest, sqlalchemy_declarative, scimark_monte_carlo, logging_format, bench_mp_pool, scimark_sparse_mat_mult
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230304-3.12.0a5+-eff9f43/bm-20230304-linux-x86_64-python-main-3.12.0a5+-eff9f43.json: comprehensions
