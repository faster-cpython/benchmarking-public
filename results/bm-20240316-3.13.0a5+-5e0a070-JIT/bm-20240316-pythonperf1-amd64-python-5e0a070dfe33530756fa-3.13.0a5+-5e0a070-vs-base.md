# Results vs. base

- fork: python
- ref: 5e0a070dfe33530756fa
- machine: windows-amd64
- commit hash: 5e0a070
- commit date: 2024-03-16
- overall geometric mean: 1.01x slower
- HPT reliability: 97.78%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240316-3.13.0a5+-5e0a070/bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070.json | results/bm-20240316-3.13.0a5+-5e0a070-JIT/bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                                                                                 | 222 ms: 1.06x slower                                                                                                       |
| chameleon      | 4.82 ms                                                                                                                | 4.74 ms: 1.02x faster                                                                                                      |
| docutils       | 1.54 sec                                                                                                               | 1.60 sec: 1.04x slower                                                                                                     |
| html5lib       | 37.0 ms                                                                                                                | 36.5 ms: 1.01x faster                                                                                                      |
| tornado_http   | 83.8 ms                                                                                                                | 85.1 ms: 1.02x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.02x slower                                                                                                               |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none, async_tree_io_tg, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240316-3.13.0a5+-5e0a070/bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070.json | results/bm-20240316-3.13.0a5+-5e0a070-JIT/bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 73.4 ms                                                                                                                | 58.2 ms: 1.26x faster                                                                                                      |
| float          | 52.6 ms                                                                                                                | 48.8 ms: 1.08x faster                                                                                                      |
| pidigits       | 147 ms                                                                                                                 | 150 ms: 1.02x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.10x faster                                                                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240316-3.13.0a5+-5e0a070/bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070.json | results/bm-20240316-3.13.0a5+-5e0a070-JIT/bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 18.1 ms                                                                                                                | 14.6 ms: 1.24x faster                                                                                                      |
| regex_dna      | 127 ms                                                                                                                 | 118 ms: 1.07x faster                                                                                                       |
| regex_effbot   | 1.62 ms                                                                                                                | 1.58 ms: 1.02x faster                                                                                                      |
| regex_compile  | 77.3 ms                                                                                                                | 83.6 ms: 1.08x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.06x faster                                                                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark           | results/bm-20240316-3.13.0a5+-5e0a070/bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070.json | results/bm-20240316-3.13.0a5+-5e0a070-JIT/bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070.json |
|---------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads         | 1.43 sec                                                                                                               | 1.19 sec: 1.20x faster                                                                                                     |
| pickle_dict         | 18.4 us                                                                                                                | 17.4 us: 1.05x faster                                                                                                      |
| xml_etree_parse     | 93.7 ms                                                                                                                | 91.0 ms: 1.03x faster                                                                                                      |
| xml_etree_iterparse | 63.0 ms                                                                                                                | 61.8 ms: 1.02x faster                                                                                                      |
| xml_etree_process   | 36.6 ms                                                                                                                | 36.2 ms: 1.01x faster                                                                                                      |
| json_dumps          | 5.57 ms                                                                                                                | 5.53 ms: 1.01x faster                                                                                                      |
| json_loads          | 13.7 us                                                                                                                | 13.6 us: 1.01x faster                                                                                                      |
| unpickle            | 8.61 us                                                                                                                | 8.56 us: 1.01x faster                                                                                                      |
| pickle              | 7.05 us                                                                                                                | 7.15 us: 1.01x slower                                                                                                      |
| pickle_pure_python  | 176 us                                                                                                                 | 178 us: 1.02x slower                                                                                                       |
| unpickle_list       | 2.71 us                                                                                                                | 2.76 us: 1.02x slower                                                                                                      |
| Geometric mean      | (ref)                                                                                                                  | 1.02x faster                                                                                                               |

Benchmark hidden because not significant (3): xml_etree_generate, unpickle_pure_python, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240316-3.13.0a5+-5e0a070/bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070.json | results/bm-20240316-3.13.0a5+-5e0a070-JIT/bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070.json |
|------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 20.5 ms                                                                                                                | 24.0 ms: 1.17x slower                                                                                                      |
| python_startup_no_site | 18.0 ms                                                                                                                | 21.8 ms: 1.21x slower                                                                                                      |
| Geometric mean         | (ref)                                                                                                                  | 1.19x slower                                                                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240316-3.13.0a5+-5e0a070/bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070.json | results/bm-20240316-3.13.0a5+-5e0a070-JIT/bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070.json |
|-----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.23 ms                                                                                                                | 5.65 ms: 1.10x faster                                                                                                      |
| genshi_text     | 16.7 ms                                                                                                                | 15.2 ms: 1.10x faster                                                                                                      |
| django_template | 21.8 ms                                                                                                                | 21.4 ms: 1.02x faster                                                                                                      |
| Geometric mean  | (ref)                                                                                                                  | 1.06x faster                                                                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | results/bm-20240316-3.13.0a5+-5e0a070/bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070.json | results/bm-20240316-3.13.0a5+-5e0a070-JIT/bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070.json |
|--------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody                    | 73.4 ms                                                                                                                | 58.2 ms: 1.26x faster                                                                                                      |
| regex_v8                 | 18.1 ms                                                                                                                | 14.6 ms: 1.24x faster                                                                                                      |
| tomli_loads              | 1.43 sec                                                                                                               | 1.19 sec: 1.20x faster                                                                                                     |
| spectral_norm            | 62.3 ms                                                                                                                | 51.8 ms: 1.20x faster                                                                                                      |
| fannkuch                 | 252 ms                                                                                                                 | 225 ms: 1.12x faster                                                                                                       |
| mako                     | 6.23 ms                                                                                                                | 5.65 ms: 1.10x faster                                                                                                      |
| genshi_text              | 16.7 ms                                                                                                                | 15.2 ms: 1.10x faster                                                                                                      |
| scimark_sparse_mat_mult  | 2.45 ms                                                                                                                | 2.24 ms: 1.09x faster                                                                                                      |
| generators               | 21.4 ms                                                                                                                | 19.7 ms: 1.08x faster                                                                                                      |
| float                    | 52.6 ms                                                                                                                | 48.8 ms: 1.08x faster                                                                                                      |
| regex_dna                | 127 ms                                                                                                                 | 118 ms: 1.07x faster                                                                                                       |
| scimark_fft              | 180 ms                                                                                                                 | 169 ms: 1.06x faster                                                                                                       |
| pickle_dict              | 18.4 us                                                                                                                | 17.4 us: 1.05x faster                                                                                                      |
| mdp                      | 1.47 sec                                                                                                               | 1.41 sec: 1.05x faster                                                                                                     |
| pprint_pformat           | 993 ms                                                                                                                 | 963 ms: 1.03x faster                                                                                                       |
| xml_etree_parse          | 93.7 ms                                                                                                                | 91.0 ms: 1.03x faster                                                                                                      |
| pprint_safe_repr         | 487 ms                                                                                                                 | 473 ms: 1.03x faster                                                                                                       |
| regex_effbot             | 1.62 ms                                                                                                                | 1.58 ms: 1.02x faster                                                                                                      |
| typing_runtime_protocols | 70.1 us                                                                                                                | 68.7 us: 1.02x faster                                                                                                      |
| django_template          | 21.8 ms                                                                                                                | 21.4 ms: 1.02x faster                                                                                                      |
| xml_etree_iterparse      | 63.0 ms                                                                                                                | 61.8 ms: 1.02x faster                                                                                                      |
| logging_format           | 6.36 us                                                                                                                | 6.25 us: 1.02x faster                                                                                                      |
| telco                    | 4.68 ms                                                                                                                | 4.60 ms: 1.02x faster                                                                                                      |
| chameleon                | 4.82 ms                                                                                                                | 4.74 ms: 1.02x faster                                                                                                      |
| comprehensions           | 10.4 us                                                                                                                | 10.3 us: 1.01x faster                                                                                                      |
| html5lib                 | 37.0 ms                                                                                                                | 36.5 ms: 1.01x faster                                                                                                      |
| sqlite_synth             | 1.60 us                                                                                                                | 1.58 us: 1.01x faster                                                                                                      |
| xml_etree_process        | 36.6 ms                                                                                                                | 36.2 ms: 1.01x faster                                                                                                      |
| logging_simple           | 5.92 us                                                                                                                | 5.86 us: 1.01x faster                                                                                                      |
| pyflate                  | 284 ms                                                                                                                 | 281 ms: 1.01x faster                                                                                                       |
| json_dumps               | 5.57 ms                                                                                                                | 5.53 ms: 1.01x faster                                                                                                      |
| json_loads               | 13.7 us                                                                                                                | 13.6 us: 1.01x faster                                                                                                      |
| unpickle                 | 8.61 us                                                                                                                | 8.56 us: 1.01x faster                                                                                                      |
| deepcopy_memo            | 21.9 us                                                                                                                | 21.9 us: 1.00x slower                                                                                                      |
| pathlib                  | 76.3 ms                                                                                                                | 76.8 ms: 1.01x slower                                                                                                      |
| crypto_pyaes             | 43.3 ms                                                                                                                | 43.7 ms: 1.01x slower                                                                                                      |
| sqlglot_normalize        | 174 ms                                                                                                                 | 175 ms: 1.01x slower                                                                                                       |
| gc_traversal             | 1.49 ms                                                                                                                | 1.51 ms: 1.01x slower                                                                                                      |
| logging_silent           | 54.4 ns                                                                                                                | 55.1 ns: 1.01x slower                                                                                                      |
| richards_super           | 30.7 ms                                                                                                                | 31.1 ms: 1.01x slower                                                                                                      |
| pickle                   | 7.05 us                                                                                                                | 7.15 us: 1.01x slower                                                                                                      |
| chaos                    | 39.1 ms                                                                                                                | 39.7 ms: 1.01x slower                                                                                                      |
| pickle_pure_python       | 176 us                                                                                                                 | 178 us: 1.02x slower                                                                                                       |
| tornado_http             | 83.8 ms                                                                                                                | 85.1 ms: 1.02x slower                                                                                                      |
| unpickle_list            | 2.71 us                                                                                                                | 2.76 us: 1.02x slower                                                                                                      |
| richards                 | 27.4 ms                                                                                                                | 27.9 ms: 1.02x slower                                                                                                      |
| aiohttp                  | 882 us                                                                                                                 | 899 us: 1.02x slower                                                                                                       |
| nqueens                  | 58.5 ms                                                                                                                | 59.7 ms: 1.02x slower                                                                                                      |
| create_gc_cycles         | 730 us                                                                                                                 | 745 us: 1.02x slower                                                                                                       |
| pidigits                 | 147 ms                                                                                                                 | 150 ms: 1.02x slower                                                                                                       |
| coverage                 | 45.4 ms                                                                                                                | 46.5 ms: 1.02x slower                                                                                                      |
| sqlglot_transpile        | 973 us                                                                                                                 | 1000 us: 1.03x slower                                                                                                      |
| scimark_monte_carlo      | 40.5 ms                                                                                                                | 41.6 ms: 1.03x slower                                                                                                      |
| meteor_contest           | 71.3 ms                                                                                                                | 73.4 ms: 1.03x slower                                                                                                      |
| async_generators         | 232 ms                                                                                                                 | 239 ms: 1.03x slower                                                                                                       |
| deltablue                | 1.97 ms                                                                                                                | 2.03 ms: 1.03x slower                                                                                                      |
| sympy_expand             | 270 ms                                                                                                                 | 279 ms: 1.03x slower                                                                                                       |
| coroutines               | 13.1 ms                                                                                                                | 13.6 ms: 1.04x slower                                                                                                      |
| sqlglot_parse            | 752 us                                                                                                                 | 781 us: 1.04x slower                                                                                                       |
| sympy_str                | 157 ms                                                                                                                 | 163 ms: 1.04x slower                                                                                                       |
| docutils                 | 1.54 sec                                                                                                               | 1.60 sec: 1.04x slower                                                                                                     |
| bench_thread_pool        | 797 us                                                                                                                 | 830 us: 1.04x slower                                                                                                       |
| sqlglot_optimize         | 33.0 ms                                                                                                                | 34.5 ms: 1.05x slower                                                                                                      |
| scimark_sor              | 79.6 ms                                                                                                                | 83.5 ms: 1.05x slower                                                                                                      |
| sympy_sum                | 82.8 ms                                                                                                                | 87.6 ms: 1.06x slower                                                                                                      |
| dulwich_log              | 39.4 ms                                                                                                                | 41.8 ms: 1.06x slower                                                                                                      |
| 2to3                     | 209 ms                                                                                                                 | 222 ms: 1.06x slower                                                                                                       |
| mypy2                    | 410 ms                                                                                                                 | 436 ms: 1.06x slower                                                                                                       |
| sympy_integrate          | 12.3 ms                                                                                                                | 13.1 ms: 1.07x slower                                                                                                      |
| regex_compile            | 77.3 ms                                                                                                                | 83.6 ms: 1.08x slower                                                                                                      |
| bench_mp_pool            | 64.4 ms                                                                                                                | 70.2 ms: 1.09x slower                                                                                                      |
| raytrace                 | 163 ms                                                                                                                 | 179 ms: 1.10x slower                                                                                                       |
| thrift                   | 8.03 ms                                                                                                                | 8.84 ms: 1.10x slower                                                                                                      |
| go                       | 84.4 ms                                                                                                                | 95.2 ms: 1.13x slower                                                                                                      |
| hexiom                   | 3.77 ms                                                                                                                | 4.28 ms: 1.13x slower                                                                                                      |
| python_startup           | 20.5 ms                                                                                                                | 24.0 ms: 1.17x slower                                                                                                      |
| python_startup_no_site   | 18.0 ms                                                                                                                | 21.8 ms: 1.21x slower                                                                                                      |
| unpack_sequence          | 36.4 ns                                                                                                                | 46.9 ns: 1.29x slower                                                                                                      |
| scimark_lu               | 55.2 ms                                                                                                                | 71.9 ms: 1.30x slower                                                                                                      |
| Geometric mean           | (ref)                                                                                                                  | 1.01x slower                                                                                                               |

Benchmark hidden because not significant (19): pycparser, genshi_xml, asyncio_tcp_ssl, xml_etree_generate, deepcopy, deepcopy_reduce, unpickle_pure_python, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none, pickle_list, async_tree_io_tg, async_tree_io, async_tree_memoization_tg, json, asyncio_tcp, pylint


# HPT report

- Reliability score: 97.78% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: unknown