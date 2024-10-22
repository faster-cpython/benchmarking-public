# Results vs. base

- fork: python
- ref: 342e654b8eda24c68da6
- machine: windows-amd64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.05x faster
- HPT reliability: 96.66%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240920-3.14.0a0-342e654/bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 225 ms                                                                                                               | 241 ms: 1.07x slower                                                                                                     |
| docutils       | 1.70 sec                                                                                                             | 1.92 sec: 1.13x slower                                                                                                   |
| html5lib       | 41.4 ms                                                                                                              | 41.9 ms: 1.01x slower                                                                                                    |
| tornado_http   | 84.6 ms                                                                                                              | 87.6 ms: 1.04x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.06x slower                                                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | results/bm-20240920-3.14.0a0-342e654/bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp_ssl        | 1.68 sec                                                                                                             | 1.37 sec: 1.22x faster                                                                                                   |
| async_tree_none        | 213 ms                                                                                                               | 206 ms: 1.04x faster                                                                                                     |
| async_tree_memoization | 265 ms                                                                                                               | 260 ms: 1.02x faster                                                                                                     |
| async_generators       | 245 ms                                                                                                               | 261 ms: 1.07x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                                | 1.01x faster                                                                                                             |

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_io_tg, coroutines, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240920-3.14.0a0-342e654/bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 85.0 ms                                                                                                              | 49.5 ms: 1.72x faster                                                                                                    |
| float          | 55.8 ms                                                                                                              | 44.3 ms: 1.26x faster                                                                                                    |
| pidigits       | 150 ms                                                                                                               | 149 ms: 1.01x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.30x faster                                                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240920-3.14.0a0-342e654/bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 117 ms                                                                                                               | 116 ms: 1.01x faster                                                                                                     |
| regex_effbot   | 1.57 ms                                                                                                              | 1.55 ms: 1.01x faster                                                                                                    |
| regex_compile  | 92.6 ms                                                                                                              | 95.0 ms: 1.03x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.02x slower                                                                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240920-3.14.0a0-342e654/bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.58 sec                                                                                                             | 1.27 sec: 1.24x faster                                                                                                   |
| xml_etree_generate   | 58.0 ms                                                                                                              | 49.4 ms: 1.17x faster                                                                                                    |
| xml_etree_process    | 41.0 ms                                                                                                              | 35.4 ms: 1.16x faster                                                                                                    |
| pickle_pure_python   | 218 us                                                                                                               | 191 us: 1.14x faster                                                                                                     |
| unpickle_pure_python | 155 us                                                                                                               | 142 us: 1.09x faster                                                                                                     |
| pickle_list          | 2.99 us                                                                                                              | 2.76 us: 1.08x faster                                                                                                    |
| unpickle             | 9.51 us                                                                                                              | 8.89 us: 1.07x faster                                                                                                    |
| xml_etree_iterparse  | 64.3 ms                                                                                                              | 60.9 ms: 1.06x faster                                                                                                    |
| pickle_dict          | 18.5 us                                                                                                              | 17.6 us: 1.05x faster                                                                                                    |
| json_dumps           | 6.16 ms                                                                                                              | 5.87 ms: 1.05x faster                                                                                                    |
| unpickle_list        | 2.75 us                                                                                                              | 2.83 us: 1.03x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.07x faster                                                                                                             |

Benchmark hidden because not significant (3): pickle, xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240920-3.14.0a0-342e654/bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 7.11 ms                                                                                                              | 5.21 ms: 1.37x faster                                                                                                    |
| django_template | 24.9 ms                                                                                                              | 26.9 ms: 1.08x slower                                                                                                    |
| genshi_text     | 17.0 ms                                                                                                              | 18.8 ms: 1.11x slower                                                                                                    |
| genshi_xml      | 35.4 ms                                                                                                              | 44.1 ms: 1.24x slower                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.02x slower                                                                                                             |

All benchmarks:
===============

| Benchmark                | results/bm-20240920-3.14.0a0-342e654/bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|--------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody                    | 85.0 ms                                                                                                              | 49.5 ms: 1.72x faster                                                                                                    |
| spectral_norm            | 70.5 ms                                                                                                              | 44.1 ms: 1.60x faster                                                                                                    |
| scimark_sor              | 92.5 ms                                                                                                              | 61.2 ms: 1.51x faster                                                                                                    |
| scimark_fft              | 212 ms                                                                                                               | 150 ms: 1.42x faster                                                                                                     |
| scimark_sparse_mat_mult  | 2.93 ms                                                                                                              | 2.09 ms: 1.40x faster                                                                                                    |
| deepcopy_memo            | 21.5 us                                                                                                              | 15.5 us: 1.39x faster                                                                                                    |
| json                     | 4.04 ms                                                                                                              | 2.94 ms: 1.38x faster                                                                                                    |
| mako                     | 7.11 ms                                                                                                              | 5.21 ms: 1.37x faster                                                                                                    |
| crypto_pyaes             | 49.2 ms                                                                                                              | 38.7 ms: 1.27x faster                                                                                                    |
| deltablue                | 2.30 ms                                                                                                              | 1.81 ms: 1.27x faster                                                                                                    |
| fannkuch                 | 300 ms                                                                                                               | 238 ms: 1.26x faster                                                                                                     |
| float                    | 55.8 ms                                                                                                              | 44.3 ms: 1.26x faster                                                                                                    |
| tomli_loads              | 1.58 sec                                                                                                             | 1.27 sec: 1.24x faster                                                                                                   |
| asyncio_tcp_ssl          | 1.68 sec                                                                                                             | 1.37 sec: 1.22x faster                                                                                                   |
| pyflate                  | 322 ms                                                                                                               | 265 ms: 1.22x faster                                                                                                     |
| scimark_monte_carlo      | 50.6 ms                                                                                                              | 42.9 ms: 1.18x faster                                                                                                    |
| xml_etree_generate       | 58.0 ms                                                                                                              | 49.4 ms: 1.17x faster                                                                                                    |
| xml_etree_process        | 41.0 ms                                                                                                              | 35.4 ms: 1.16x faster                                                                                                    |
| scimark_lu               | 61.7 ms                                                                                                              | 54.0 ms: 1.14x faster                                                                                                    |
| telco                    | 5.39 ms                                                                                                              | 4.73 ms: 1.14x faster                                                                                                    |
| pickle_pure_python       | 218 us                                                                                                               | 191 us: 1.14x faster                                                                                                     |
| comprehensions           | 11.9 us                                                                                                              | 10.6 us: 1.12x faster                                                                                                    |
| logging_silent           | 63.4 ns                                                                                                              | 56.7 ns: 1.12x faster                                                                                                    |
| chaos                    | 44.2 ms                                                                                                              | 40.0 ms: 1.10x faster                                                                                                    |
| unpickle_pure_python     | 155 us                                                                                                               | 142 us: 1.09x faster                                                                                                     |
| pprint_safe_repr         | 548 ms                                                                                                               | 503 ms: 1.09x faster                                                                                                     |
| pickle_list              | 2.99 us                                                                                                              | 2.76 us: 1.08x faster                                                                                                    |
| pprint_pformat           | 1.12 sec                                                                                                             | 1.04 sec: 1.08x faster                                                                                                   |
| unpickle                 | 9.51 us                                                                                                              | 8.89 us: 1.07x faster                                                                                                    |
| meteor_contest           | 78.4 ms                                                                                                              | 73.5 ms: 1.07x faster                                                                                                    |
| logging_simple           | 6.42 us                                                                                                              | 6.04 us: 1.06x faster                                                                                                    |
| logging_format           | 6.91 us                                                                                                              | 6.52 us: 1.06x faster                                                                                                    |
| xml_etree_iterparse      | 64.3 ms                                                                                                              | 60.9 ms: 1.06x faster                                                                                                    |
| pickle_dict              | 18.5 us                                                                                                              | 17.6 us: 1.05x faster                                                                                                    |
| pycparser                | 747 ms                                                                                                               | 709 ms: 1.05x faster                                                                                                     |
| json_dumps               | 6.16 ms                                                                                                              | 5.87 ms: 1.05x faster                                                                                                    |
| deepcopy                 | 193 us                                                                                                               | 184 us: 1.04x faster                                                                                                     |
| async_tree_none          | 213 ms                                                                                                               | 206 ms: 1.04x faster                                                                                                     |
| nqueens                  | 64.4 ms                                                                                                              | 62.4 ms: 1.03x faster                                                                                                    |
| mdp                      | 1.45 sec                                                                                                             | 1.41 sec: 1.03x faster                                                                                                   |
| deepcopy_reduce          | 1.94 us                                                                                                              | 1.88 us: 1.03x faster                                                                                                    |
| coverage                 | 47.3 ms                                                                                                              | 46.1 ms: 1.03x faster                                                                                                    |
| thrift                   | 525 us                                                                                                               | 513 us: 1.02x faster                                                                                                     |
| sqlglot_parse            | 896 us                                                                                                               | 880 us: 1.02x faster                                                                                                     |
| async_tree_memoization   | 265 ms                                                                                                               | 260 ms: 1.02x faster                                                                                                     |
| raytrace                 | 201 ms                                                                                                               | 197 ms: 1.02x faster                                                                                                     |
| dulwich_log              | 43.2 ms                                                                                                              | 42.6 ms: 1.01x faster                                                                                                    |
| regex_dna                | 117 ms                                                                                                               | 116 ms: 1.01x faster                                                                                                     |
| sqlite_synth             | 1.62 us                                                                                                              | 1.60 us: 1.01x faster                                                                                                    |
| regex_effbot             | 1.57 ms                                                                                                              | 1.55 ms: 1.01x faster                                                                                                    |
| pidigits                 | 150 ms                                                                                                               | 149 ms: 1.01x faster                                                                                                     |
| pathlib                  | 75.6 ms                                                                                                              | 76.1 ms: 1.01x slower                                                                                                    |
| gc_traversal             | 1.53 ms                                                                                                              | 1.54 ms: 1.01x slower                                                                                                    |
| html5lib                 | 41.4 ms                                                                                                              | 41.9 ms: 1.01x slower                                                                                                    |
| create_gc_cycles         | 884 us                                                                                                               | 899 us: 1.02x slower                                                                                                     |
| typing_runtime_protocols | 111 us                                                                                                               | 114 us: 1.03x slower                                                                                                     |
| regex_compile            | 92.6 ms                                                                                                              | 95.0 ms: 1.03x slower                                                                                                    |
| unpickle_list            | 2.75 us                                                                                                              | 2.83 us: 1.03x slower                                                                                                    |
| sqlglot_transpile        | 1.12 ms                                                                                                              | 1.15 ms: 1.03x slower                                                                                                    |
| tornado_http             | 84.6 ms                                                                                                              | 87.6 ms: 1.04x slower                                                                                                    |
| go                       | 87.6 ms                                                                                                              | 91.3 ms: 1.04x slower                                                                                                    |
| sqlglot_normalize        | 192 ms                                                                                                               | 201 ms: 1.04x slower                                                                                                     |
| sympy_str                | 179 ms                                                                                                               | 188 ms: 1.05x slower                                                                                                     |
| sympy_expand             | 310 ms                                                                                                               | 330 ms: 1.06x slower                                                                                                     |
| async_generators         | 245 ms                                                                                                               | 261 ms: 1.07x slower                                                                                                     |
| richards_super           | 36.1 ms                                                                                                              | 38.6 ms: 1.07x slower                                                                                                    |
| 2to3                     | 225 ms                                                                                                               | 241 ms: 1.07x slower                                                                                                     |
| bench_mp_pool            | 66.4 ms                                                                                                              | 71.7 ms: 1.08x slower                                                                                                    |
| django_template          | 24.9 ms                                                                                                              | 26.9 ms: 1.08x slower                                                                                                    |
| sympy_sum                | 90.7 ms                                                                                                              | 98.3 ms: 1.08x slower                                                                                                    |
| generators               | 21.2 ms                                                                                                              | 23.1 ms: 1.09x slower                                                                                                    |
| hexiom                   | 4.46 ms                                                                                                              | 4.87 ms: 1.09x slower                                                                                                    |
| genshi_text              | 17.0 ms                                                                                                              | 18.8 ms: 1.11x slower                                                                                                    |
| sqlglot_optimize         | 36.4 ms                                                                                                              | 40.3 ms: 1.11x slower                                                                                                    |
| sympy_integrate          | 13.3 ms                                                                                                              | 14.8 ms: 1.11x slower                                                                                                    |
| richards                 | 32.1 ms                                                                                                              | 36.1 ms: 1.12x slower                                                                                                    |
| docutils                 | 1.70 sec                                                                                                             | 1.92 sec: 1.13x slower                                                                                                   |
| pylint                   | 225 ms                                                                                                               | 264 ms: 1.17x slower                                                                                                     |
| genshi_xml               | 35.4 ms                                                                                                              | 44.1 ms: 1.24x slower                                                                                                    |
| unpack_sequence          | 43.1 ns                                                                                                              | 58.0 ns: 1.34x slower                                                                                                    |
| Geometric mean           | (ref)                                                                                                                | 1.05x faster                                                                                                             |

Benchmark hidden because not significant (15): async_tree_none_tg, bench_thread_pool, async_tree_io_tg, python_startup, pickle, xml_etree_parse, coroutines, async_tree_cpu_io_mixed_tg, json_loads, async_tree_io, python_startup_no_site, async_tree_memoization_tg, async_tree_cpu_io_mixed, asyncio_tcp, regex_v8

# HPT report

- Reliability score: 96.66% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown