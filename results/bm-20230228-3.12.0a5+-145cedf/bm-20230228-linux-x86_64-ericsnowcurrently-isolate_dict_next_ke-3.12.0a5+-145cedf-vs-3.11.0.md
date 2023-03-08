
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: isolate_dict_next_ke
- machine: linux-x86_64
- commit hash: 145cedf
- commit date: 2023-02-28
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                              |
| docutils       | 2.60 sec                                               | 2.55 sec: 1.02x faster                                                            |
| html5lib       | 64.8 ms                                                | 62.5 ms: 1.04x faster                                                             |
| tornado_http   | 96.5 ms                                                | 95.2 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                      |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 75.1 ms: 1.02x faster                                                             |
| pidigits       | 197 ms                                                 | 193 ms: 1.02x faster                                                              |
| nbody          | 90.0 ms                                                | 93.6 ms: 1.04x slower                                                             |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8       | 22.2 ms                                                | 21.7 ms: 1.02x faster                                                             |
| regex_dna      | 203 ms                                                 | 200 ms: 1.02x faster                                                              |
| regex_compile  | 136 ms                                                 | 134 ms: 1.02x faster                                                              |
| regex_effbot   | 3.46 ms                                                | 3.62 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.59 ms: 1.29x faster                                                             |
| unpickle_pure_python | 227 us                                                 | 203 us: 1.12x faster                                                              |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                              |
| json_loads           | 26.1 us                                                | 24.2 us: 1.08x faster                                                             |
| pickle_pure_python   | 308 us                                                 | 290 us: 1.06x faster                                                              |
| xml_etree_iterparse  | 104 ms                                                 | 100 ms: 1.04x faster                                                              |
| pickle_dict          | 31.2 us                                                | 31.5 us: 1.01x slower                                                             |
| pickle_list          | 4.14 us                                                | 4.22 us: 1.02x slower                                                             |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                                             |
| unpickle             | 13.3 us                                                | 13.8 us: 1.04x slower                                                             |
| xml_etree_process    | 53.7 ms                                                | 56.0 ms: 1.04x slower                                                             |
| unpickle_list        | 4.99 us                                                | 5.29 us: 1.06x slower                                                             |
| xml_etree_generate   | 75.9 ms                                                | 81.8 ms: 1.08x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 9.07 ms: 1.06x slower                                                             |
| python_startup_no_site | 6.04 ms                                                | 6.57 ms: 1.09x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 48.0 ms: 1.07x faster                                                             |
| mako            | 9.83 ms                                                | 10.0 ms: 1.02x slower                                                             |
| django_template | 32.3 ms                                                | 33.8 ms: 1.04x slower                                                             |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                                      |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.8 ms: 2.39x faster                                                             |
| asyncio_tcp             | 883 ms                                                 | 500 ms: 1.77x faster                                                              |
| json_dumps              | 12.4 ms                                                | 9.59 ms: 1.29x faster                                                             |
| mypy2                   | 420 ms                                                 | 334 ms: 1.26x faster                                                              |
| deltablue               | 3.66 ms                                                | 3.25 ms: 1.13x faster                                                             |
| coroutines              | 26.2 ms                                                | 23.4 ms: 1.12x faster                                                             |
| unpickle_pure_python    | 227 us                                                 | 203 us: 1.12x faster                                                              |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                                              |
| pycparser               | 1.19 sec                                               | 1.10 sec: 1.08x faster                                                            |
| json_loads              | 26.1 us                                                | 24.2 us: 1.08x faster                                                             |
| genshi_xml              | 51.4 ms                                                | 48.0 ms: 1.07x faster                                                             |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.07x faster                                                              |
| json                    | 4.87 ms                                                | 4.58 ms: 1.06x faster                                                             |
| pickle_pure_python      | 308 us                                                 | 290 us: 1.06x faster                                                              |
| fannkuch                | 384 ms                                                 | 362 ms: 1.06x faster                                                              |
| coverage                | 99.3 ms                                                | 95.0 ms: 1.04x faster                                                             |
| richards                | 46.1 ms                                                | 44.2 ms: 1.04x faster                                                             |
| scimark_fft             | 325 ms                                                 | 312 ms: 1.04x faster                                                              |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.40 ms: 1.04x faster                                                             |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                                             |
| html5lib                | 64.8 ms                                                | 62.5 ms: 1.04x faster                                                             |
| xml_etree_iterparse     | 104 ms                                                 | 100 ms: 1.04x faster                                                              |
| spectral_norm           | 98.1 ms                                                | 94.8 ms: 1.04x faster                                                             |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                                              |
| sqlglot_optimize        | 52.7 ms                                                | 51.1 ms: 1.03x faster                                                             |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.03x faster                                                            |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                              |
| pprint_safe_repr        | 706 ms                                                 | 685 ms: 1.03x faster                                                              |
| sympy_expand            | 475 ms                                                 | 462 ms: 1.03x faster                                                              |
| hexiom                  | 6.34 ms                                                | 6.16 ms: 1.03x faster                                                             |
| logging_simple          | 6.02 us                                                | 5.86 us: 1.03x faster                                                             |
| gunicorn                | 1.12 ms                                                | 1.09 ms: 1.03x faster                                                             |
| crypto_pyaes            | 75.7 ms                                                | 73.8 ms: 1.03x faster                                                             |
| nqueens                 | 83.8 ms                                                | 81.8 ms: 1.02x faster                                                             |
| regex_v8                | 22.2 ms                                                | 21.7 ms: 1.02x faster                                                             |
| chaos                   | 68.7 ms                                                | 67.1 ms: 1.02x faster                                                             |
| deepcopy_memo           | 35.8 us                                                | 35.0 us: 1.02x faster                                                             |
| float                   | 76.8 ms                                                | 75.1 ms: 1.02x faster                                                             |
| bench_thread_pool       | 817 us                                                 | 799 us: 1.02x faster                                                              |
| pidigits                | 197 ms                                                 | 193 ms: 1.02x faster                                                              |
| logging_silent          | 98.0 ns                                                | 96.0 ns: 1.02x faster                                                             |
| docutils                | 2.60 sec                                               | 2.55 sec: 1.02x faster                                                            |
| unpack_sequence         | 44.5 ns                                                | 43.6 ns: 1.02x faster                                                             |
| regex_dna               | 203 ms                                                 | 200 ms: 1.02x faster                                                              |
| regex_compile           | 136 ms                                                 | 134 ms: 1.02x faster                                                              |
| dulwich_log             | 64.0 ms                                                | 63.1 ms: 1.01x faster                                                             |
| sympy_str               | 291 ms                                                 | 287 ms: 1.01x faster                                                              |
| tornado_http            | 96.5 ms                                                | 95.2 ms: 1.01x faster                                                             |
| sympy_integrate         | 21.0 ms                                                | 20.7 ms: 1.01x faster                                                             |
| logging_format          | 6.48 us                                                | 6.39 us: 1.01x faster                                                             |
| go                      | 140 ms                                                 | 139 ms: 1.01x faster                                                              |
| deepcopy                | 341 us                                                 | 337 us: 1.01x faster                                                              |
| telco                   | 6.43 ms                                                | 6.36 ms: 1.01x faster                                                             |
| create_gc_cycles        | 1.52 ms                                                | 1.50 ms: 1.01x faster                                                             |
| async_tree_io           | 1.30 sec                                               | 1.29 sec: 1.01x faster                                                            |
| deepcopy_reduce         | 3.02 us                                                | 3.00 us: 1.01x faster                                                             |
| gc_traversal            | 3.82 ms                                                | 3.84 ms: 1.00x slower                                                             |
| mdp                     | 2.63 sec                                               | 2.65 sec: 1.01x slower                                                            |
| raytrace                | 291 ms                                                 | 295 ms: 1.01x slower                                                              |
| pickle_dict             | 31.2 us                                                | 31.5 us: 1.01x slower                                                             |
| thrift                  | 760 us                                                 | 770 us: 1.01x slower                                                              |
| sympy_sum               | 166 ms                                                 | 169 ms: 1.02x slower                                                              |
| async_tree_cpu_io_mixed | 736 ms                                                 | 749 ms: 1.02x slower                                                              |
| pickle_list             | 4.14 us                                                | 4.22 us: 1.02x slower                                                             |
| mako                    | 9.83 ms                                                | 10.0 ms: 1.02x slower                                                             |
| scimark_lu              | 108 ms                                                 | 110 ms: 1.02x slower                                                              |
| pyflate                 | 419 ms                                                 | 429 ms: 1.02x slower                                                              |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                                             |
| nbody                   | 90.0 ms                                                | 93.6 ms: 1.04x slower                                                             |
| scimark_monte_carlo     | 68.0 ms                                                | 70.7 ms: 1.04x slower                                                             |
| async_tree_memoization  | 624 ms                                                 | 650 ms: 1.04x slower                                                              |
| unpickle                | 13.3 us                                                | 13.8 us: 1.04x slower                                                             |
| xml_etree_process       | 53.7 ms                                                | 56.0 ms: 1.04x slower                                                             |
| django_template         | 32.3 ms                                                | 33.8 ms: 1.04x slower                                                             |
| regex_effbot            | 3.46 ms                                                | 3.62 ms: 1.05x slower                                                             |
| sqlglot_transpile       | 1.65 ms                                                | 1.74 ms: 1.05x slower                                                             |
| python_startup          | 8.58 ms                                                | 9.07 ms: 1.06x slower                                                             |
| unpickle_list           | 4.99 us                                                | 5.29 us: 1.06x slower                                                             |
| sqlite_synth            | 2.48 us                                                | 2.63 us: 1.06x slower                                                             |
| sqlglot_parse           | 1.36 ms                                                | 1.45 ms: 1.06x slower                                                             |
| xml_etree_generate      | 75.9 ms                                                | 81.8 ms: 1.08x slower                                                             |
| python_startup_no_site  | 6.04 ms                                                | 6.57 ms: 1.09x slower                                                             |
| async_generators        | 356 ms                                                 | 423 ms: 1.19x slower                                                              |
| dask                    | 365 ms                                                 | 509 ms: 1.39x slower                                                              |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                      |

Benchmark hidden because not significant (9): meteor_contest, async_tree_none, pathlib, sqlalchemy_imperative, djangocms, bench_mp_pool, genshi_text, sqlalchemy_declarative, chameleon
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230228-3.12.0a5+-145cedf/bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf.json: comprehensions
