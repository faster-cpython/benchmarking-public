
# Results vs. 3.11.0

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: fa5965d
- commit date: 2023-02-02
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.04x faster                                                       |
| chameleon      | 6.38 ms                                                | 6.26 ms: 1.02x faster                                                      |
| docutils       | 2.60 sec                                               | 2.49 sec: 1.04x faster                                                     |
| html5lib       | 64.8 ms                                                | 60.1 ms: 1.08x faster                                                      |
| tornado_http   | 96.5 ms                                                | 94.3 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 71.9 ms: 1.07x faster                                                      |
| pidigits       | 197 ms                                                 | 198 ms: 1.00x slower                                                       |
| nbody          | 90.0 ms                                                | 98.9 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.07x faster                                                       |
| regex_v8       | 22.2 ms                                                | 21.7 ms: 1.03x faster                                                      |
| regex_effbot   | 3.46 ms                                                | 3.40 ms: 1.02x faster                                                      |
| regex_dna      | 203 ms                                                 | 210 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.40 ms: 1.31x faster                                                      |
| unpickle_pure_python | 227 us                                                 | 198 us: 1.15x faster                                                       |
| json_loads           | 26.1 us                                                | 23.9 us: 1.09x faster                                                      |
| pickle_pure_python   | 308 us                                                 | 285 us: 1.08x faster                                                       |
| xml_etree_parse      | 160 ms                                                 | 149 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                       |
| xml_etree_process    | 53.7 ms                                                | 53.1 ms: 1.01x faster                                                      |
| pickle_dict          | 31.2 us                                                | 31.0 us: 1.00x faster                                                      |
| xml_etree_generate   | 75.9 ms                                                | 76.7 ms: 1.01x slower                                                      |
| unpickle_list        | 4.99 us                                                | 5.07 us: 1.02x slower                                                      |
| pickle               | 9.90 us                                                | 10.3 us: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                               |

Benchmark hidden because not significant (2): unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.72 ms: 1.02x slower                                                      |
| python_startup_no_site | 6.04 ms                                                | 6.25 ms: 1.03x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.8 ms: 1.08x faster                                                      |
| mako            | 9.83 ms                                                | 9.53 ms: 1.03x faster                                                      |
| genshi_text     | 21.5 ms                                                | 21.3 ms: 1.01x faster                                                      |
| django_template | 32.3 ms                                                | 32.9 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 496 ms: 1.78x faster                                                       |
| json_dumps              | 12.4 ms                                                | 9.40 ms: 1.31x faster                                                      |
| unpickle_pure_python    | 227 us                                                 | 198 us: 1.15x faster                                                       |
| deltablue               | 3.66 ms                                                | 3.21 ms: 1.14x faster                                                      |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.08 ms: 1.12x faster                                                      |
| nqueens                 | 83.8 ms                                                | 75.8 ms: 1.10x faster                                                      |
| richards                | 46.1 ms                                                | 42.2 ms: 1.09x faster                                                      |
| json_loads              | 26.1 us                                                | 23.9 us: 1.09x faster                                                      |
| pickle_pure_python      | 308 us                                                 | 285 us: 1.08x faster                                                       |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.08x faster                                                       |
| html5lib                | 64.8 ms                                                | 60.1 ms: 1.08x faster                                                      |
| genshi_xml              | 51.4 ms                                                | 47.8 ms: 1.08x faster                                                      |
| sympy_str               | 291 ms                                                 | 271 ms: 1.08x faster                                                       |
| xml_etree_parse         | 160 ms                                                 | 149 ms: 1.08x faster                                                       |
| scimark_fft             | 325 ms                                                 | 304 ms: 1.07x faster                                                       |
| regex_compile           | 136 ms                                                 | 128 ms: 1.07x faster                                                       |
| hexiom                  | 6.34 ms                                                | 5.93 ms: 1.07x faster                                                      |
| float                   | 76.8 ms                                                | 71.9 ms: 1.07x faster                                                      |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                                       |
| logging_silent          | 98.0 ns                                                | 92.0 ns: 1.07x faster                                                      |
| chaos                   | 68.7 ms                                                | 64.5 ms: 1.06x faster                                                      |
| fannkuch                | 384 ms                                                 | 361 ms: 1.06x faster                                                       |
| pyflate                 | 419 ms                                                 | 394 ms: 1.06x faster                                                       |
| sympy_integrate         | 21.0 ms                                                | 19.8 ms: 1.06x faster                                                      |
| json                    | 4.87 ms                                                | 4.60 ms: 1.06x faster                                                      |
| deepcopy_memo           | 35.8 us                                                | 34.0 us: 1.05x faster                                                      |
| bench_thread_pool       | 817 us                                                 | 777 us: 1.05x faster                                                       |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.05x faster                                                      |
| sympy_expand            | 475 ms                                                 | 455 ms: 1.05x faster                                                       |
| go                      | 140 ms                                                 | 134 ms: 1.05x faster                                                       |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                                     |
| pprint_safe_repr        | 706 ms                                                 | 676 ms: 1.04x faster                                                       |
| docutils                | 2.60 sec                                               | 2.49 sec: 1.04x faster                                                     |
| scimark_monte_carlo     | 68.0 ms                                                | 65.2 ms: 1.04x faster                                                      |
| pycparser               | 1.19 sec                                               | 1.14 sec: 1.04x faster                                                     |
| create_gc_cycles        | 1.52 ms                                                | 1.46 ms: 1.04x faster                                                      |
| crypto_pyaes            | 75.7 ms                                                | 73.1 ms: 1.04x faster                                                      |
| deepcopy                | 341 us                                                 | 329 us: 1.04x faster                                                       |
| deepcopy_reduce         | 3.02 us                                                | 2.91 us: 1.04x faster                                                      |
| 2to3                    | 259 ms                                                 | 251 ms: 1.04x faster                                                       |
| sqlglot_optimize        | 52.7 ms                                                | 50.9 ms: 1.04x faster                                                      |
| raytrace                | 291 ms                                                 | 282 ms: 1.03x faster                                                       |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.03x faster                                                      |
| logging_simple          | 6.02 us                                                | 5.83 us: 1.03x faster                                                      |
| mako                    | 9.83 ms                                                | 9.53 ms: 1.03x faster                                                      |
| scimark_lu              | 108 ms                                                 | 105 ms: 1.03x faster                                                       |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                       |
| mdp                     | 2.63 sec                                               | 2.56 sec: 1.03x faster                                                     |
| regex_v8                | 22.2 ms                                                | 21.7 ms: 1.03x faster                                                      |
| coroutines              | 26.2 ms                                                | 25.5 ms: 1.03x faster                                                      |
| tornado_http            | 96.5 ms                                                | 94.3 ms: 1.02x faster                                                      |
| thrift                  | 760 us                                                 | 743 us: 1.02x faster                                                       |
| unpack_sequence         | 44.5 ns                                                | 43.5 ns: 1.02x faster                                                      |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                       |
| chameleon               | 6.38 ms                                                | 6.26 ms: 1.02x faster                                                      |
| telco                   | 6.43 ms                                                | 6.33 ms: 1.02x faster                                                      |
| regex_effbot            | 3.46 ms                                                | 3.40 ms: 1.02x faster                                                      |
| spectral_norm           | 98.1 ms                                                | 96.8 ms: 1.01x faster                                                      |
| genshi_text             | 21.5 ms                                                | 21.3 ms: 1.01x faster                                                      |
| dulwich_log             | 64.0 ms                                                | 63.3 ms: 1.01x faster                                                      |
| pathlib                 | 18.1 ms                                                | 17.9 ms: 1.01x faster                                                      |
| xml_etree_process       | 53.7 ms                                                | 53.1 ms: 1.01x faster                                                      |
| logging_format          | 6.48 us                                                | 6.42 us: 1.01x faster                                                      |
| async_generators        | 356 ms                                                 | 354 ms: 1.00x faster                                                       |
| pickle_dict             | 31.2 us                                                | 31.0 us: 1.00x faster                                                      |
| pidigits                | 197 ms                                                 | 198 ms: 1.00x slower                                                       |
| xml_etree_generate      | 75.9 ms                                                | 76.7 ms: 1.01x slower                                                      |
| meteor_contest          | 104 ms                                                 | 106 ms: 1.01x slower                                                       |
| unpickle_list           | 4.99 us                                                | 5.07 us: 1.02x slower                                                      |
| python_startup          | 8.58 ms                                                | 8.72 ms: 1.02x slower                                                      |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.02x slower                                                     |
| django_template         | 32.3 ms                                                | 32.9 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed | 736 ms                                                 | 755 ms: 1.03x slower                                                       |
| sqlglot_transpile       | 1.65 ms                                                | 1.69 ms: 1.03x slower                                                      |
| sqlglot_parse           | 1.36 ms                                                | 1.40 ms: 1.03x slower                                                      |
| python_startup_no_site  | 6.04 ms                                                | 6.25 ms: 1.03x slower                                                      |
| regex_dna               | 203 ms                                                 | 210 ms: 1.04x slower                                                       |
| pickle                  | 9.90 us                                                | 10.3 us: 1.04x slower                                                      |
| sqlite_synth            | 2.48 us                                                | 2.60 us: 1.05x slower                                                      |
| gc_traversal            | 3.82 ms                                                | 4.06 ms: 1.06x slower                                                      |
| generators              | 73.5 ms                                                | 78.1 ms: 1.06x slower                                                      |
| async_tree_memoization  | 624 ms                                                 | 667 ms: 1.07x slower                                                       |
| nbody                   | 90.0 ms                                                | 98.9 ms: 1.10x slower                                                      |
| dask                    | 365 ms                                                 | 499 ms: 1.37x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (6): unpickle, djangocms, async_tree_none, bench_mp_pool, pickle_list, coverage
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230202-3.12.0a4+-fa5965d/bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d.json: mypy
