
# Results vs. 3.11.0

- fork: faster-cpython
- ref: pep_669_incremental
- machine: linux-x86_64
- commit hash: 5629a3e
- commit date: 2023-02-17
- overall geometric mean: 1.05x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-5629a3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 244 ms: 1.06x faster                                                            |
| chameleon      | 6.38 ms                                                | 6.33 ms: 1.01x faster                                                           |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                          |
| html5lib       | 64.8 ms                                                | 59.7 ms: 1.09x faster                                                           |
| tornado_http   | 96.5 ms                                                | 93.3 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-5629a3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.4 ms: 1.06x faster                                                           |
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                                            |
| nbody          | 90.0 ms                                                | 92.4 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-5629a3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 125 ms: 1.09x faster                                                            |
| regex_dna      | 203 ms                                                 | 205 ms: 1.01x slower                                                            |
| regex_v8       | 22.2 ms                                                | 22.5 ms: 1.01x slower                                                           |
| regex_effbot   | 3.46 ms                                                | 3.65 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-5629a3e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.37 ms: 1.32x faster                                                           |
| unpickle_pure_python | 227 us                                                 | 193 us: 1.17x faster                                                            |
| pickle_pure_python   | 308 us                                                 | 279 us: 1.11x faster                                                            |
| json_loads           | 26.1 us                                                | 23.7 us: 1.10x faster                                                           |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.09x faster                                                            |
| xml_etree_iterparse  | 104 ms                                                 | 100 ms: 1.04x faster                                                            |
| pickle_dict          | 31.2 us                                                | 30.8 us: 1.01x faster                                                           |
| unpickle_list        | 4.99 us                                                | 5.08 us: 1.02x slower                                                           |
| xml_etree_process    | 53.7 ms                                                | 55.0 ms: 1.02x slower                                                           |
| pickle_list          | 4.14 us                                                | 4.25 us: 1.03x slower                                                           |
| unpickle             | 13.3 us                                                | 13.7 us: 1.04x slower                                                           |
| pickle               | 9.90 us                                                | 10.3 us: 1.04x slower                                                           |
| xml_etree_generate   | 75.9 ms                                                | 80.3 ms: 1.06x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-5629a3e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.97 ms: 1.05x slower                                                           |
| python_startup_no_site | 6.04 ms                                                | 6.52 ms: 1.08x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-5629a3e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.0 ms: 1.12x faster                                                           |
| genshi_text     | 21.5 ms                                                | 20.6 ms: 1.05x faster                                                           |
| mako            | 9.83 ms                                                | 9.76 ms: 1.01x faster                                                           |
| django_template | 32.3 ms                                                | 33.1 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                                    |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-5629a3e |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.8 ms: 2.39x faster                                                           |
| asyncio_tcp             | 883 ms                                                 | 501 ms: 1.76x faster                                                            |
| json_dumps              | 12.4 ms                                                | 9.37 ms: 1.32x faster                                                           |
| mypy2                   | 420 ms                                                 | 325 ms: 1.29x faster                                                            |
| coroutines              | 26.2 ms                                                | 21.1 ms: 1.24x faster                                                           |
| unpickle_pure_python    | 227 us                                                 | 193 us: 1.17x faster                                                            |
| deltablue               | 3.66 ms                                                | 3.13 ms: 1.17x faster                                                           |
| genshi_xml              | 51.4 ms                                                | 46.0 ms: 1.12x faster                                                           |
| pickle_pure_python      | 308 us                                                 | 279 us: 1.11x faster                                                            |
| richards                | 46.1 ms                                                | 41.9 ms: 1.10x faster                                                           |
| json_loads              | 26.1 us                                                | 23.7 us: 1.10x faster                                                           |
| sympy_str               | 291 ms                                                 | 265 ms: 1.10x faster                                                            |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.20 ms: 1.09x faster                                                           |
| nqueens                 | 83.8 ms                                                | 76.9 ms: 1.09x faster                                                           |
| regex_compile           | 136 ms                                                 | 125 ms: 1.09x faster                                                            |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.09x faster                                                            |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.09x faster                                                            |
| html5lib                | 64.8 ms                                                | 59.7 ms: 1.09x faster                                                           |
| fannkuch                | 384 ms                                                 | 356 ms: 1.08x faster                                                            |
| sympy_integrate         | 21.0 ms                                                | 19.5 ms: 1.07x faster                                                           |
| deepcopy_memo           | 35.8 us                                                | 33.4 us: 1.07x faster                                                           |
| mdp                     | 2.63 sec                                               | 2.46 sec: 1.07x faster                                                          |
| scimark_fft             | 325 ms                                                 | 305 ms: 1.07x faster                                                            |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                                            |
| chaos                   | 68.7 ms                                                | 64.5 ms: 1.06x faster                                                           |
| gc_traversal            | 3.82 ms                                                | 3.59 ms: 1.06x faster                                                           |
| 2to3                    | 259 ms                                                 | 244 ms: 1.06x faster                                                            |
| float                   | 76.8 ms                                                | 72.4 ms: 1.06x faster                                                           |
| sympy_expand            | 475 ms                                                 | 449 ms: 1.06x faster                                                            |
| spectral_norm           | 98.1 ms                                                | 92.7 ms: 1.06x faster                                                           |
| hexiom                  | 6.34 ms                                                | 5.99 ms: 1.06x faster                                                           |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                                          |
| go                      | 140 ms                                                 | 133 ms: 1.06x faster                                                            |
| json                    | 4.87 ms                                                | 4.62 ms: 1.05x faster                                                           |
| logging_simple          | 6.02 us                                                | 5.72 us: 1.05x faster                                                           |
| pprint_safe_repr        | 706 ms                                                 | 671 ms: 1.05x faster                                                            |
| unpack_sequence         | 44.5 ns                                                | 42.4 ns: 1.05x faster                                                           |
| deepcopy                | 341 us                                                 | 325 us: 1.05x faster                                                            |
| aiohttp                 | 1.05 ms                                                | 1000 us: 1.05x faster                                                           |
| gunicorn                | 1.12 ms                                                | 1.06 ms: 1.05x faster                                                           |
| pycparser               | 1.19 sec                                               | 1.13 sec: 1.05x faster                                                          |
| bench_thread_pool       | 817 us                                                 | 779 us: 1.05x faster                                                            |
| genshi_text             | 21.5 ms                                                | 20.6 ms: 1.05x faster                                                           |
| pyflate                 | 419 ms                                                 | 401 ms: 1.04x faster                                                            |
| dulwich_log             | 64.0 ms                                                | 61.2 ms: 1.04x faster                                                           |
| logging_silent          | 98.0 ns                                                | 93.8 ns: 1.04x faster                                                           |
| crypto_pyaes            | 75.7 ms                                                | 72.6 ms: 1.04x faster                                                           |
| scimark_monte_carlo     | 68.0 ms                                                | 65.2 ms: 1.04x faster                                                           |
| sqlglot_normalize       | 108 ms                                                 | 103 ms: 1.04x faster                                                            |
| sqlglot_optimize        | 52.7 ms                                                | 50.6 ms: 1.04x faster                                                           |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                                            |
| deepcopy_reduce         | 3.02 us                                                | 2.90 us: 1.04x faster                                                           |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                          |
| raytrace                | 291 ms                                                 | 280 ms: 1.04x faster                                                            |
| xml_etree_iterparse     | 104 ms                                                 | 100 ms: 1.04x faster                                                            |
| tornado_http            | 96.5 ms                                                | 93.3 ms: 1.03x faster                                                           |
| sqlalchemy_imperative   | 18.1 ms                                                | 17.6 ms: 1.03x faster                                                           |
| sqlalchemy_declarative  | 138 ms                                                 | 135 ms: 1.03x faster                                                            |
| create_gc_cycles        | 1.52 ms                                                | 1.48 ms: 1.02x faster                                                           |
| logging_format          | 6.48 us                                                | 6.33 us: 1.02x faster                                                           |
| meteor_contest          | 104 ms                                                 | 102 ms: 1.02x faster                                                            |
| async_tree_none         | 526 ms                                                 | 518 ms: 1.02x faster                                                            |
| pickle_dict             | 31.2 us                                                | 30.8 us: 1.01x faster                                                           |
| chameleon               | 6.38 ms                                                | 6.33 ms: 1.01x faster                                                           |
| mako                    | 9.83 ms                                                | 9.76 ms: 1.01x faster                                                           |
| regex_dna               | 203 ms                                                 | 205 ms: 1.01x slower                                                            |
| pathlib                 | 18.1 ms                                                | 18.2 ms: 1.01x slower                                                           |
| regex_v8                | 22.2 ms                                                | 22.5 ms: 1.01x slower                                                           |
| unpickle_list           | 4.99 us                                                | 5.08 us: 1.02x slower                                                           |
| async_tree_cpu_io_mixed | 736 ms                                                 | 750 ms: 1.02x slower                                                            |
| xml_etree_process       | 53.7 ms                                                | 55.0 ms: 1.02x slower                                                           |
| django_template         | 32.3 ms                                                | 33.1 ms: 1.02x slower                                                           |
| pickle_list             | 4.14 us                                                | 4.25 us: 1.03x slower                                                           |
| nbody                   | 90.0 ms                                                | 92.4 ms: 1.03x slower                                                           |
| sqlglot_transpile       | 1.65 ms                                                | 1.69 ms: 1.03x slower                                                           |
| sqlglot_parse           | 1.36 ms                                                | 1.41 ms: 1.03x slower                                                           |
| unpickle                | 13.3 us                                                | 13.7 us: 1.04x slower                                                           |
| pickle                  | 9.90 us                                                | 10.3 us: 1.04x slower                                                           |
| sqlite_synth            | 2.48 us                                                | 2.59 us: 1.04x slower                                                           |
| python_startup          | 8.58 ms                                                | 8.97 ms: 1.05x slower                                                           |
| async_tree_memoization  | 624 ms                                                 | 655 ms: 1.05x slower                                                            |
| regex_effbot            | 3.46 ms                                                | 3.65 ms: 1.06x slower                                                           |
| xml_etree_generate      | 75.9 ms                                                | 80.3 ms: 1.06x slower                                                           |
| python_startup_no_site  | 6.04 ms                                                | 6.52 ms: 1.08x slower                                                           |
| async_generators        | 356 ms                                                 | 422 ms: 1.19x slower                                                            |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                                    |

Benchmark hidden because not significant (7): telco, async_tree_io, djangocms, coverage, scimark_lu, bench_mp_pool, thrift
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: dask, flaskblogging, pylint
