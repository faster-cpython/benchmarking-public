
# Results vs. 3.11.0

- fork: barneygale
- ref: optimize_pathlib_par
- machine: linux-x86_64
- commit hash: d5231b6
- commit date: 2023-02-04
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230204-linux-x86_64-barneygale-optimize_pathlib_par-3.12.0a4+-d5231b6 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                       |
| chameleon      | 6.38 ms                                                | 6.27 ms: 1.02x faster                                                      |
| docutils       | 2.60 sec                                               | 2.51 sec: 1.04x faster                                                     |
| html5lib       | 64.8 ms                                                | 60.4 ms: 1.07x faster                                                      |
| tornado_http   | 96.5 ms                                                | 93.7 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230204-linux-x86_64-barneygale-optimize_pathlib_par-3.12.0a4+-d5231b6 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.2 ms: 1.06x faster                                                      |
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                                       |
| nbody          | 90.0 ms                                                | 92.6 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230204-linux-x86_64-barneygale-optimize_pathlib_par-3.12.0a4+-d5231b6 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 127 ms: 1.07x faster                                                       |
| regex_v8       | 22.2 ms                                                | 22.6 ms: 1.02x slower                                                      |
| regex_effbot   | 3.46 ms                                                | 3.59 ms: 1.04x slower                                                      |
| regex_dna      | 203 ms                                                 | 216 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230204-linux-x86_64-barneygale-optimize_pathlib_par-3.12.0a4+-d5231b6 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.22 ms: 1.34x faster                                                      |
| unpickle_pure_python | 227 us                                                 | 197 us: 1.15x faster                                                       |
| pickle_pure_python   | 308 us                                                 | 280 us: 1.10x faster                                                       |
| xml_etree_parse      | 160 ms                                                 | 146 ms: 1.10x faster                                                       |
| json_loads           | 26.1 us                                                | 23.9 us: 1.09x faster                                                      |
| pickle_dict          | 31.2 us                                                | 30.6 us: 1.02x faster                                                      |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                       |
| pickle_list          | 4.14 us                                                | 4.17 us: 1.01x slower                                                      |
| xml_etree_process    | 53.7 ms                                                | 54.0 ms: 1.01x slower                                                      |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                                      |
| xml_etree_generate   | 75.9 ms                                                | 77.7 ms: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                               |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230204-linux-x86_64-barneygale-optimize_pathlib_par-3.12.0a4+-d5231b6 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.91 ms: 1.04x slower                                                      |
| python_startup_no_site | 6.04 ms                                                | 6.44 ms: 1.07x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230204-linux-x86_64-barneygale-optimize_pathlib_par-3.12.0a4+-d5231b6 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.5 ms: 1.11x faster                                                      |
| genshi_text     | 21.5 ms                                                | 20.8 ms: 1.04x faster                                                      |
| mako            | 9.83 ms                                                | 9.74 ms: 1.01x faster                                                      |
| django_template | 32.3 ms                                                | 32.6 ms: 1.01x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230204-linux-x86_64-barneygale-optimize_pathlib_par-3.12.0a4+-d5231b6 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 489 ms: 1.81x faster                                                       |
| json_dumps              | 12.4 ms                                                | 9.22 ms: 1.34x faster                                                      |
| unpickle_pure_python    | 227 us                                                 | 197 us: 1.15x faster                                                       |
| scimark_sparse_mat_mult | 4.59 ms                                                | 3.99 ms: 1.15x faster                                                      |
| deltablue               | 3.66 ms                                                | 3.19 ms: 1.15x faster                                                      |
| genshi_xml              | 51.4 ms                                                | 46.5 ms: 1.11x faster                                                      |
| pickle_pure_python      | 308 us                                                 | 280 us: 1.10x faster                                                       |
| xml_etree_parse         | 160 ms                                                 | 146 ms: 1.10x faster                                                       |
| richards                | 46.1 ms                                                | 42.3 ms: 1.09x faster                                                      |
| json_loads              | 26.1 us                                                | 23.9 us: 1.09x faster                                                      |
| nqueens                 | 83.8 ms                                                | 77.0 ms: 1.09x faster                                                      |
| gc_traversal            | 3.82 ms                                                | 3.53 ms: 1.08x faster                                                      |
| sympy_str               | 291 ms                                                 | 269 ms: 1.08x faster                                                       |
| chaos                   | 68.7 ms                                                | 63.6 ms: 1.08x faster                                                      |
| scimark_fft             | 325 ms                                                 | 302 ms: 1.08x faster                                                       |
| mdp                     | 2.63 sec                                               | 2.44 sec: 1.08x faster                                                     |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.07x faster                                                       |
| html5lib                | 64.8 ms                                                | 60.4 ms: 1.07x faster                                                      |
| fannkuch                | 384 ms                                                 | 359 ms: 1.07x faster                                                       |
| regex_compile           | 136 ms                                                 | 127 ms: 1.07x faster                                                       |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                                       |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.06x faster                                                     |
| float                   | 76.8 ms                                                | 72.2 ms: 1.06x faster                                                      |
| pprint_safe_repr        | 706 ms                                                 | 666 ms: 1.06x faster                                                       |
| sympy_integrate         | 21.0 ms                                                | 19.8 ms: 1.06x faster                                                      |
| pyflate                 | 419 ms                                                 | 397 ms: 1.06x faster                                                       |
| coroutines              | 26.2 ms                                                | 24.8 ms: 1.05x faster                                                      |
| aiohttp                 | 1.05 ms                                                | 995 us: 1.05x faster                                                       |
| logging_simple          | 6.02 us                                                | 5.72 us: 1.05x faster                                                      |
| hexiom                  | 6.34 ms                                                | 6.03 ms: 1.05x faster                                                      |
| json                    | 4.87 ms                                                | 4.63 ms: 1.05x faster                                                      |
| scimark_monte_carlo     | 68.0 ms                                                | 65.1 ms: 1.04x faster                                                      |
| coverage                | 99.3 ms                                                | 95.1 ms: 1.04x faster                                                      |
| sympy_expand            | 475 ms                                                 | 456 ms: 1.04x faster                                                       |
| logging_silent          | 98.0 ns                                                | 94.0 ns: 1.04x faster                                                      |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                                       |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.04x faster                                                      |
| bench_thread_pool       | 817 us                                                 | 785 us: 1.04x faster                                                       |
| deepcopy                | 341 us                                                 | 328 us: 1.04x faster                                                       |
| spectral_norm           | 98.1 ms                                                | 94.5 ms: 1.04x faster                                                      |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                                       |
| raytrace                | 291 ms                                                 | 281 ms: 1.04x faster                                                       |
| deepcopy_memo           | 35.8 us                                                | 34.5 us: 1.04x faster                                                      |
| genshi_text             | 21.5 ms                                                | 20.8 ms: 1.04x faster                                                      |
| docutils                | 2.60 sec                                               | 2.51 sec: 1.04x faster                                                     |
| unpack_sequence         | 44.5 ns                                                | 43.1 ns: 1.03x faster                                                      |
| create_gc_cycles        | 1.52 ms                                                | 1.47 ms: 1.03x faster                                                      |
| crypto_pyaes            | 75.7 ms                                                | 73.4 ms: 1.03x faster                                                      |
| sqlglot_optimize        | 52.7 ms                                                | 51.1 ms: 1.03x faster                                                      |
| pycparser               | 1.19 sec                                               | 1.15 sec: 1.03x faster                                                     |
| tornado_http            | 96.5 ms                                                | 93.7 ms: 1.03x faster                                                      |
| deepcopy_reduce         | 3.02 us                                                | 2.93 us: 1.03x faster                                                      |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                       |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.02x faster                                                       |
| dulwich_log             | 64.0 ms                                                | 62.8 ms: 1.02x faster                                                      |
| pickle_dict             | 31.2 us                                                | 30.6 us: 1.02x faster                                                      |
| logging_format          | 6.48 us                                                | 6.36 us: 1.02x faster                                                      |
| chameleon               | 6.38 ms                                                | 6.27 ms: 1.02x faster                                                      |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                       |
| async_generators        | 356 ms                                                 | 350 ms: 1.02x faster                                                       |
| thrift                  | 760 us                                                 | 752 us: 1.01x faster                                                       |
| mako                    | 9.83 ms                                                | 9.74 ms: 1.01x faster                                                      |
| pickle_list             | 4.14 us                                                | 4.17 us: 1.01x slower                                                      |
| xml_etree_process       | 53.7 ms                                                | 54.0 ms: 1.01x slower                                                      |
| django_template         | 32.3 ms                                                | 32.6 ms: 1.01x slower                                                      |
| generators              | 73.5 ms                                                | 74.2 ms: 1.01x slower                                                      |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                                      |
| regex_v8                | 22.2 ms                                                | 22.6 ms: 1.02x slower                                                      |
| scimark_lu              | 108 ms                                                 | 110 ms: 1.02x slower                                                       |
| xml_etree_generate      | 75.9 ms                                                | 77.7 ms: 1.02x slower                                                      |
| nbody                   | 90.0 ms                                                | 92.6 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed | 736 ms                                                 | 757 ms: 1.03x slower                                                       |
| regex_effbot            | 3.46 ms                                                | 3.59 ms: 1.04x slower                                                      |
| python_startup          | 8.58 ms                                                | 8.91 ms: 1.04x slower                                                      |
| sqlglot_transpile       | 1.65 ms                                                | 1.72 ms: 1.04x slower                                                      |
| async_tree_memoization  | 624 ms                                                 | 654 ms: 1.05x slower                                                       |
| pathlib                 | 18.1 ms                                                | 19.0 ms: 1.05x slower                                                      |
| sqlglot_parse           | 1.36 ms                                                | 1.43 ms: 1.05x slower                                                      |
| sqlite_synth            | 2.48 us                                                | 2.61 us: 1.05x slower                                                      |
| regex_dna               | 203 ms                                                 | 216 ms: 1.06x slower                                                       |
| python_startup_no_site  | 6.04 ms                                                | 6.44 ms: 1.07x slower                                                      |
| dask                    | 365 ms                                                 | 498 ms: 1.36x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (8): djangocms, meteor_contest, telco, async_tree_none, unpickle_list, bench_mp_pool, async_tree_io, unpickle
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230204-3.12.0a4+-d5231b6/bm-20230204-linux-x86_64-barneygale-optimize_pathlib_par-3.12.0a4+-d5231b6.json: mypy
